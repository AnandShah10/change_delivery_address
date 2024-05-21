from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def open_wizard(self):
        # self.ensure_one()
        view_id = self.env.ref('change_delivery_address.change_delivery_address_form')
        print(view_id,'View')
        print(self.partner_id.id)
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'change.delivery.address',
            'view_id': view_id.id,
            'target': 'new',
            'context': {'partner_id': self.partner_id.id},
        }
