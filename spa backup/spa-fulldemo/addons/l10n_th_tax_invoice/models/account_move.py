# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
import calendar
import datetime
from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare

from dateutil.relativedelta import relativedelta


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    def _create_tax_cash_basis_moves(self):
        move_lines = self.debit_move_id | self.credit_move_id
        payment = move_lines.mapped("payment_id")
        if len(payment) == 1:
            self = self.with_context(payment_id=payment.id)
        return super()._create_tax_cash_basis_moves()


class AccountMoveTaxInvoice(models.Model):
    _name = "account.move.tax.invoice"
    _description = "Tax Invoice Info"

    tax_invoice_number = fields.Char(string="Tax Invoice Number", copy=False)
    tax_invoice_date = fields.Date(string="Tax Invoice Date", copy=False)
    report_late_mo = fields.Selection(
        [
            ("0", "0 month"),
            ("1", "1 month"),
            ("2", "2 months"),
            ("3", "3 months"),
            ("4", "4 months"),
            ("5", "5 months"),
            ("6", "6 months"),
        ],
        string="Report Late",
        default="0",
        required=True,
    )
    report_date = fields.Date(
        string="Report Date",
        compute="_compute_report_date",
        store=True,
    )
    move_line_id = fields.Many2one(
        comodel_name="account.move.line", index=True, copy=True, ondelete="cascade"
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        ondelete="restrict",
    )
    move_id = fields.Many2one(comodel_name="account.move", index=True, copy=True)
    move_state = fields.Selection(related="move_id.state", store=True)
    payment_id = fields.Many2one(
        comodel_name="account.payment",
        compute="_compute_payment_id",
        store=True,
        copy=True,
    )
    to_clear_tax = fields.Boolean(related="payment_id.to_clear_tax")
    company_id = fields.Many2one(
        comodel_name="res.company", related="move_id.company_id", store=True
    )
    company_currency_id = fields.Many2one(
        comodel_name="res.currency", related="company_id.currency_id"
    )
    account_id = fields.Many2one(
        comodel_name="account.account", related="move_line_id.account_id"
    )
    tax_line_id = fields.Many2one(
        comodel_name="account.tax", related="move_line_id.tax_line_id"
    )
    tax_base_amount = fields.Monetary(
        "Tax Base", currency_field="company_currency_id", copy=False
    )
    balance = fields.Monetary(
        "Tax Amount", currency_field="company_currency_id", copy=False
    )
    reversing_id = fields.Many2one(
        comodel_name="account.move", help="The move that reverse this move"
    )
    reversed_id = fields.Many2one(
        comodel_name="account.move", help="This move that this move reverse"
    )

    @api.depends("move_line_id")
    def _compute_payment_id(self):
        for rec in self:
            if not rec.payment_id:
                origin_move = rec.move_id.reversed_entry_id
                payment = origin_move.tax_invoice_ids.mapped("payment_id")
                rec.payment_id = (
                    payment and payment.id or self._context.get("payment_id", False)
                )

    @api.depends("report_late_mo", "tax_invoice_date")
    def _compute_report_date(self):
        for rec in self:
            if rec.tax_invoice_date:
                eval_date = rec.tax_invoice_date + relativedelta(
                    months=int(rec.report_late_mo)
                )
                last_date = calendar.monthrange(eval_date.year, eval_date.month)[1]
                rec.report_date = datetime.date(
                    eval_date.year, eval_date.month, last_date
                )
            else:
                rec.report_date = False

    def unlink(self):
        """Do not allow remove the last tax_invoice of move_line"""
        line_taxinv = {}
        for move_line in self.mapped("move_line_id"):
            line_taxinv.update({move_line.id: move_line.tax_invoice_ids.ids})
        for rec in self.filtered("move_line_id"):
            if len(line_taxinv[rec.move_line_id.id]) == 1 and not self._context.get(
                "force_remove_tax_invoice"
            ):
                raise UserError(_("Cannot delete this last tax invoice line"))
            line_taxinv[rec.move_line_id.id].remove(rec.id)
        return super().unlink()


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    tax_invoice_ids = fields.One2many(
        comodel_name="account.move.tax.invoice", inverse_name="move_line_id"
    )
    manual_tax_invoice = fields.Boolean(
        copy=False, help="Create Tax Invoice for this debit/credit line"
    )
    tax_exigible = fields.Boolean(string='Appears in VAT report', default=True, readonly=True,
        help="Technical field used to mark a tax line as exigible in the vat report or not (only exigible journal items"
             " are displayed). By default all new journal items are directly exigible, but with the feature cash_basis"
             " on taxes, some will become exigible only when the payment is recorded.")

    def _checkout_tax_invoice_amount(self):
        for line in self:
            if not line.manual_tax_invoice and line.tax_invoice_ids:
                tax = sum(line.tax_invoice_ids.mapped("balance"))
                if float_compare(abs(line.balance), abs(tax), 2) != 0:
                    raise UserError(_("Invalid Tax Amount"))

    @api.model_create_multi
    def create(self, vals_list):
        move_lines = super().create(vals_list)
        TaxInvoice = self.env["account.move.tax.invoice"]
        sign = self._context.get("reverse_tax_invoice") and -1 or 1
        for line in move_lines:
            if (line.tax_line_id and line.tax_exigible) or line.manual_tax_invoice:
                taxinv = TaxInvoice.create(
                    {
                        "move_id": line.move_id.id,
                        "move_line_id": line.id,
                        "partner_id": line.partner_id.id,
                        "tax_invoice_number": sign < 0 and "/" or False,
                        "tax_invoice_date": sign < 0 and fields.Date.today() or False,
                        "tax_base_amount": sign * abs(line.tax_base_amount),
                        "balance": sign * abs(line.balance),
                        "reversed_id": (
                            line.move_id.move_type == "entry"
                            and line.move_id.reversed_entry_id.id
                            or False
                        ),
                    }
                )
                line.tax_invoice_ids |= taxinv
            for taxinv in line.tax_invoice_ids.filtered("reversed_id"):
                TaxInvoice.search([("move_id", "=", taxinv.reversed_id.id)]).write(
                    {"reversing_id": taxinv.move_id.id}
                )
        return move_lines

    def write(self, vals):
        if "manual_tax_invoice" in vals:
            if vals["manual_tax_invoice"]:
                TaxInvoice = self.env["account.move.tax.invoice"]
                for line in self:
                    taxinv = TaxInvoice.create(
                        {
                            "move_id": line.move_id.id,
                            "move_line_id": line.id,
                            "partner_id": line.partner_id.id,
                            "tax_base_amount": abs(line.tax_base_amount),
                            "balance": abs(line.balance),
                        }
                    )
                    line.tax_invoice_ids |= taxinv
            else:
                self = self.with_context(force_remove_tax_invoice=True)
                self.mapped("tax_invoice_ids").unlink()
        return super().write(vals)


class AccountMove(models.Model):
    _inherit = "account.move"

    tax_invoice_ids = fields.One2many(
        comodel_name="account.move.tax.invoice",
        inverse_name="move_id",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=False,
    )

    def _post(self, soft=True):
        for move in self:
            for tax_invoice in move.tax_invoice_ids.filtered(
                lambda l: l.tax_line_id.type_tax_use == "purchase"
                or (
                    l.move_id.move_type == "entry"
                    and not l.payment_id
                    and l.move_id.journal_id.type != "sale"
                )
            ):
                if (
                    not tax_invoice.tax_invoice_number
                    or not tax_invoice.tax_invoice_date
                ):
                    if tax_invoice.payment_id:  # Defer posting for payment
                        tax_invoice.payment_id.write({"to_clear_tax": True})
                        return self.browse()  # return False
                    elif self.mapped("move_type") == ["entry", "entry"]:
                        return self.browse()  # return False
                    else:
                        raise UserError(_("Please fill in tax invoice and tax date"))
        res = super()._post(soft)

        for move in self:
            for tax_invoice in move.tax_invoice_ids.filtered(
                lambda l: l.tax_line_id.type_tax_use == "sale"
                or l.move_id.journal_id.type == "sale"
            ):
                tinv_number, tinv_date = self._get_tax_invoice_number(
                    move, tax_invoice, tax_invoice.tax_line_id
                )
                tax_invoice.write(
                    {"tax_invoice_number": tinv_number, "tax_invoice_date": tinv_date}
                )

        # Check amount tax invoice with move line
        for move in self:
            move.line_ids._checkout_tax_invoice_amount()
        return res

    def _get_tax_invoice_number(self, move, tax_invoice, tax):
        origin_move = move.move_type == "entry" and move.reversed_entry_id or move
        sequence = tax_invoice.tax_line_id.taxinv_sequence_id
        number = tax_invoice.tax_invoice_number
        invoice_date = tax_invoice.tax_invoice_date or origin_move.date
        if move.move_type in ("out_invoice", "out_refund"):
            number = False if number in (False, "/") else number
        if not number:
            if sequence:
                if move != origin_move:  # Case reversed entry, use origin
                    tax_invoices = origin_move.tax_invoice_ids.filtered(
                        lambda l: l.tax_line_id == tax
                    )
                    number = (
                        tax_invoices and tax_invoices[0].tax_invoice_number or False
                    )
                    if not number:
                        raise ValidationError(
                            _("Cannot set tax invoice number, number already exists.")
                        )
                else:  # Normal case, use new sequence
                    number = sequence.next_by_id(sequence_date=move.date)
            else:  # Now sequence for this tax, use document number
                number = tax_invoice.payment_id.name or origin_move.name
        return (number, invoice_date)

    def _reverse_moves(self, default_values_list=None, cancel=False):
        self = self.with_context(reverse_tax_invoice=True)
        return super()._reverse_moves(
            default_values_list=default_values_list, cancel=cancel
        )
