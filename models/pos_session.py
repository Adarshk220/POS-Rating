from odoo import models


class PosSession(models.Model):
    """Extends the pos session"""
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('product_rating')
        return result
