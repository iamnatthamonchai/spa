from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http

class SaleController(WebsiteSale):
    @http.route(auth='user')
    def checkout(self, **post):
         #the user is logged in to checkout
         return super(SaleController, self).checkout(**post)
