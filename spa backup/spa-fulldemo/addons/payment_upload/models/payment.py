# -*- coding: utf-8 -*-

import base64
from odoo import api, fields, models, _
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare

import logging
import pprint

from promptpay import qrcode

_logger = logging.getLogger(__name__)


class TransferPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[
        ('transfer', 'Manual Payment')
    ], default='transfer', ondelete={'transfer': 'set default'})

    qr_code_promptpay = fields.Boolean("Use PromptPay QR code")
    promptpay_id = fields.Char(
        string="PromptPay ID",
        help="13 digits for company's tax ID or 10 digits for mobile phone number",
    )
    bank_name = fields.Char(
        string="Bank Name",
        help="Name of the bank"
    )
    bank_account_number = fields.Char(
        string="Bank Account Number"
    )
    bank_account_holder_name = fields.Char(
        string="Bank Account Holder Name"
    )

    @api.model
    def _create_missing_journal_for_acquirers(self, company=None):
        # By default, the wire transfer method uses the default Bank journal.
        company = company or self.env.company
        acquirers = self.env['payment.acquirer'].search(
            [('provider', '=', 'transfer'), ('journal_id', '=', False), ('company_id', '=', company.id)])

        bank_journal = self.env['account.journal'].search(
            [('type', '=', 'bank'), ('company_id', '=', company.id)], limit=1)
        if bank_journal:
            acquirers.write({'journal_id': bank_journal.id})
        return super(TransferPaymentAcquirer, self)._create_missing_journal_for_acquirers(company=company)

    def promptpayPayload(self, amount):
        return qrcode.generate_payload(self.promptpay_id, float(amount))

    def transfer_get_form_action_url(self):
        return '/payment/transfer/upload/feedback'

    def _format_transfer_data(self):
        company_id = self.env.company.id
        # filter only bank accounts marked as visible
        journals = self.env['account.journal'].search([('type', '=', 'bank'), ('company_id', '=', company_id)])
        accounts = journals.mapped('bank_account_id').name_get()
        bank_title = _('Bank Accounts') if len(accounts) > 1 else _('Bank Account')
        bank_accounts = ''.join(['<ul>'] + ['<li>%s</li>' % name for id, name in accounts] + ['</ul>'])
        post_msg = _('''<div>
<h3>Please use the following transfer details</h3>
<h4>%(bank_title)s</h4>
%(bank_accounts)s
<h4>Communication</h4>
<p>Please use the order name as communication reference.</p>
</div>''') % {
            'bank_title': bank_title,
            'bank_accounts': bank_accounts,
        }
        return post_msg

    @api.model
    def create(self, values):
        """ Hook in create to create a default pending_msg. This is done in create
        to have access to the name and other creation values. If no pending_msg
        or a void pending_msg is given at creation, generate a default one. """
        if values.get('provider') == 'transfer' and not values.get('pending_msg'):
            values['pending_msg'] = self._format_transfer_data()
        return super(TransferPaymentAcquirer, self).create(values)

    def write(self, values):
        """ Hook in write to create a default pending_msg. See create(). """
        if not values.get('pending_msg', False) and all(not acquirer.pending_msg and acquirer.provider != 'transfer' for acquirer in self) and values.get('provider') == 'transfer':
            values['pending_msg'] = self._format_transfer_data()
        return super(TransferPaymentAcquirer, self).write(values)


class TransferPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    payment_slip_attachment = fields.Image('slip_attachment', max_width=1024)

    def _automate_sale_order(self, tx):
        for sale_order in tx.sale_order_ids:
            sale_order.action_confirm()

    @api.model
    def _transfer_form_get_tx_from_data(self, data):
        payment_tx_id, reference, amount, currency_name = data.get('payment_tx_id'), data.get('reference'), data.get('amount'), data.get('currency_name')

        if payment_tx_id:
            tx = self.search([('id', '=', payment_tx_id)])
            file_data = data.get('payment_slip_image').read()
            tx.write({'payment_slip_attachment': base64.encodebytes(file_data)})
            self._automate_sale_order(tx)
            tx._set_transaction_done()
        else:
            tx = self.search([('reference', '=', reference)])

        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            raise ValidationError(error_msg)

        return tx

    def _transfer_form_get_invalid_parameters(self, data):
        invalid_parameters = []

        if float_compare(float(data.get('amount') or '0.0'), self.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        if data.get('currency') != self.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        return invalid_parameters

    def _transfer_form_validate(self, data):
        _logger.info('Validated transfer payment for tx %s: set as pending' % (self.reference))
        self._set_transaction_pending()
        return True
