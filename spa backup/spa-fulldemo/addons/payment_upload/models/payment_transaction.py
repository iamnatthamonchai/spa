# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models, _
from odoo.addons.payment_transfer.controllers.main import TransferController
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare

import logging
import pprint


_logger = logging.getLogger(__name__)


class UploadPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    payment_slip_attachment = fields.Image('slip_attachment', max_width=1024)

    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return Transfer-specific rendering values.

        Note: self.ensure_one() from `_get_processing_values`

        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of acquirer-specific processing values
        :rtype: dict
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider != 'transfer':
            return res

        return {
            'api_url': TransferController._accept_url,
            'reference': self.reference,
        }

    @api.model
    def _get_tx_from_feedback_data(self, provider, data):
        tx = super()._get_tx_from_feedback_data(provider, data)
        if provider != 'transfer':
            return tx

        reference = data.get('reference')
        tx = self.search([('reference', '=', reference), ('provider', '=', 'transfer')])
        if not tx:
            raise ValidationError(
                "Upload Transfer: " + _("No transaction found matching reference %s.", reference)
            )

        slip_image = data.get('payment_slip_image', None)
        if slip_image:
            file_data = slip_image.read()
            tx.write({'payment_slip_attachment': base64.encodebytes(file_data)})
            self._automate_sale_order(tx)
            self._set_done()
            tx._set_done()
        return tx

    def _process_feedback_data(self, data):
        """ Override of payment to process the transaction based on transfer data.

        Note: self.ensure_one()

        :param dict data: The transfer feedback data
        :return: None
        """
        super()._process_feedback_data(data)
        if self.provider != 'transfer':
            return

        _logger.info(
            "validated upload payment for tx with reference %s: set as pending", self.reference
        )
        self._set_pending()

    def _log_received_message(self):
        """ Override of payment to remove transfer acquirer from the recordset.

        :return: None
        """
        other_provider_txs = self.filtered(lambda t: t.provider != 'transfer')
        super(UploadPaymentTransaction, other_provider_txs)._log_received_message()

    def _get_sent_message(self):
        """ Override of payment to return a different message.

        :return: The 'transaction sent' message
        :rtype: str
        """
        message = super()._get_sent_message()
        if self.provider == 'transfer':
            message = _(
                "The customer has selected %(acq_name)s to make the payment.",
                acq_name=self.acquirer_id.name
            )
        return message


    def _automate_sale_order(self, tx):
        for sale_order in tx.sale_order_ids:
            sale_order.action_confirm()
