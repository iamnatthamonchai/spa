import logging
from odoo import api, fields, models,exceptions

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    """Override SaleOrder to perform action_confirm"""
    _inherit = "sale.order"

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if not order.invoice_ids:
                order._create_invoices()

            if order.invoice_ids:
                for invoice in order.invoice_ids:
                    if invoice.amount_total > 0:
                        invoice.action_post()
        return res
