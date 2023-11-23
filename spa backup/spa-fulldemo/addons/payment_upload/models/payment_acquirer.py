from odoo import api, fields, models, _

import logging
import pprint

# from promptpay import qrcode

_logger = logging.getLogger(__name__)


class TransferPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[
        ('transfer', 'Upload Payment')
    ], default='upload', ondelete={'upload': 'set default'})

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

    # @api.model
    # def _create_missing_journal_for_acquirers(self, company=None):
    #     # By default, the wire transfer method uses the default Bank journal.
    #     company = company or self.env.company
    #     acquirers = self.env['payment.acquirer'].search(
    #         [('provider', '=', 'transfer'), ('journal_id', '=', False), ('company_id', '=', company.id)])
    #
    #     bank_journal = self.env['account.journal'].search(
    #         [('type', '=', 'bank'), ('company_id', '=', company.id)], limit=1)
    #     if bank_journal:
    #         acquirers.write({'journal_id': bank_journal.id})
    #     return super(TransferPaymentAcquirer, self)._create_missing_journal_for_acquirers(company=company)

    @api.depends('provider')
    def _compute_view_configuration_fields(self):
        """ Override of payment to hide the credentials page.

        :return: None
        """
        super()._compute_view_configuration_fields()
        self.filtered(lambda acq: acq.provider == 'transfer').write({
            'show_credentials_page': False,
            'show_payment_icon_ids': False,
            'show_pre_msg': False,
            'show_done_msg': False,
            'show_cancel_msg': False,
        })

    def promptpayPayload(self, amount):
        return qrcode.generate_payload(self.promptpay_id, float(amount))

    def _transfer_ensure_pending_msg_is_set(self):
        for acquirer in self.filtered(lambda a: a.provider == 'transfer' and not a.pending_msg):
            company_id = acquirer.company_id.id
            # filter only bank accounts marked as visible
            accounts = self.env['account.journal'].search([
                ('type', '=', 'bank'), ('company_id', '=', company_id)
            ]).bank_account_id
            acquirer.pending_msg = f'<div>' \
                f'<h3>{_("Please use the following transfer details")}</h3>' \
                f'<h4>{_("Bank Account") if len(accounts) == 1 else _("Bank Accounts")}</h4>' \
                f'<ul>{"".join(f"<li>{account.display_name}</li>" for account in accounts)}</ul>' \
                f'<h4>{_("Communication")}</h4>' \
                f'<p>{_("Please use the order name as communication reference.")}</p>' \
                f'</div>'

    @api.model_create_multi
    def create(self, values_list):
        """ Make sure to have a pending_msg set. """
        # This is done here and not in a default to have access to all required values.
        acquirers = super().create(values_list)
        acquirers._transfer_ensure_pending_msg_is_set()
        return acquirers

    def write(self, values):
        """ Make sure to have a pending_msg set. """
        # This is done here and not in a default to have access to all required values.
        res = super().write(values)
        self._transfer_ensure_pending_msg_is_set()
        return res
