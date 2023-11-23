# -*- coding: utf-8 -*-
import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class TransferController(http.Controller):
    _accept_url = '/payment/upload/feedback'

    @http.route([
        '/payment/upload/feedback',
    ], type='http', auth='public', csrf=False)
    def transfer_form_feedback(self, **post):
        # _logger.info("++++++++++++++++++++++++++++++++++++++++")
        # _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))  # debug
        # _logger.info('Env : %s', pprint.pformat(request.env['payment.transaction']))
        # _logger.info("++++++++++++++++++++++++++++++++++++++++")
        request.env['payment.transaction'].sudo()._handle_feedback_data('transfer', post)
        return werkzeug.utils.redirect('/payment/process')


class PaymentSlipUploadController(http.Controller):
    _accept_url = '/payment/transfer/upload/payment-slip'

    @http.route([
        '/payment/transfer/upload/payment-slip',
    ], type='http', auth='public', website=True)
    def handle_upload(self, **post):
        # _logger.info("========================================")
        # _logger.info('Handle file uploading %s', pprint.pformat(post))  # debug
        # _logger.info('Env : %s', pprint.pformat(post['return_url']))
        # _logger.info("========================================")
        request.env['payment.transaction'].sudo()._handle_feedback_data('transfer', post)
        return werkzeug.utils.redirect(post['return_url'])
