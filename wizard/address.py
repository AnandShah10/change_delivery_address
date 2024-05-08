from odoo import models, fields, api, _
from lxml import etree


class ChangeDeliveryAddress(models.TransientModel):
    _name = 'change.delivery.address'
    _description = 'Change the delivery address of sale order'
    _rec_name = 'address'

    # partner_id = fields.Many2one('res.partner', compute='_compute_customer')
    # addr = fields.Many2many('res.partner', compute='_compute_addr', search='_search_addr')
    address = fields.Many2one('res.partner', string='Address',
                              domain=[('type', '=', 'delivery')])

    # def _compute_addr(self):
    #     active_id = self._context.get('active_id')
    #     if active_id:
    #         print('active is here.....................', active_id)
    #         order = self.env['sale.order'].browse(active_id)
    #         partner_id = order.partner_id.id
    #         self.addr = [
    #             (6, 0, self.env['res.partner'].search([('type', '=', 'delivery'), ('parent_id', '=', partner_id)]).ids)]
    #
    # def _search_addr(self):
    #     active_id = self._context.get('active_id')
    #     if active_id:
    #         print('active is here.....................', active_id)
    #         order = self.env['sale.order'].browse(active_id)
    #         partner_id = order.partner_id.id
    #         return [('parent_id', '=', partner_id), ('type', '=', 'delivery')]
    #     else:
    #         return [('type', '=', 'delivery')]

    def change_deliver_address(self):
        print("hello!!!!!!!!!!!!!!1")
        print(self.env.context)
        order = self.env['sale.order'].browse(self.env.context['active_id'])
        print(order)
        order.write({'partner_shipping_id': self.address.id})

    # def search_fetch(self, domain, field_names, offset=0, limit=None, order=None):
    #     print("hello search fetch",domain,field_names,'###############################')
    #     return super().search_fetch(domain, field_names, offset, limit, order)

    # @api.model
    # def default_get(self, fields):
    #     print('In here!!!!!!!!!!!!!!!!!!!!!!')
    #     # self.modified(['address'])
    #     """
    #     Override default_get method to dynamically set domain for address field.
    #     """
    #     print(self.fields_get(['address']), '***********************Address')
    #     res = super(ChangeDeliveryAddress, self).default_get(fields)
    #     print("Done with the response..........................", res)
    #     active_id = self._context.get('active_id')
    #     if active_id:
    #         print('active is here.....................', active_id)
    #         order = self.env['sale.order'].browse(active_id)
    #         partner_id = order.partner_id.id
    #         print('Partner@@@@@@@@@@@@@@@@@@@', partner_id)
    #         if partner_id:
    #             res.update({'address': partner_id})
    #             print("here...............................")
    #             domain = [('type', '=', 'delivery'), ('parent_id', '=', partner_id)]
    #             print(self.fields_get(['address']), '***********************Address')
    #             print(self.fields_get(['address'])['address'], '__________________Address')
    #             print(self.fields_get(['address'])['address']['domain'], '***********************Domain')
    #             # self.fields_get(['address'])['address'].update({'domain': domain})
    #             # print(self.fields_get(['address'])['address']['domain'], ',,,,,,,,,,,,,Domain Again')
    #             # self.fields_get(['address'])['address']['domain'] = domain
    #             print(self.fields_get(['address'])['address']['domain'], ',,,,,,,,,,,,,Domain Again2')
    #             # self.env.context = dict(self.env.context, address_domain=domain)
    #             # print(self.env.context, 'Context...............')
    #             print(res, 'Response again...............')
    #             # self.filtered_domain(domain)
    #     return res

    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     print(attributes,'Attributes')
    #     print('fields here entered@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    #     """ Hide analytic_distribution_search from filterable/searchable fields"""
    #     active_id = self._context.get('active_id')
    #     domain = [('type', '=', 'delivery')]
    #     if active_id:
    #         print('active is here.....................', active_id)
    #         order = self.env['sale.order'].browse(active_id)
    #         partner_id = order.partner_id
    #         print('Partner@@@@@@@@@@@@@@@@@@@', partner_id)
    #         if partner_id:
    #             # res.update({'address': partner_id})
    #             print("here...............................")
    #             domain = f"[('type', '=', 'delivery'), ('parent_id', '=', {partner_id.id})]"
    #
    #     res = super(ChangeDeliveryAddress,self).fields_get(allfields, attributes)
    #     print('response of fields!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #     if res.get('address'):
    #         print(res.get('address'), 'address here11111111111111111111111111')
    #         res['address']['domain'] = domain
    #         print(res['address']['domain'], 'Field domain')
    #
    #     return res

    # @api.onchange('address')
    # def change_domain_on_change(self):
    #     print('On change is heree will it work?')
    #     active_id = self._context.get('active_id')
    #     domain = [('type', '=', 'delivery')]
    #     if active_id:
    #         print('active is here.....................', active_id)
    #         order = self.env['sale.order'].browse(active_id)
    #         partner_id = order.partner_id
    #         print('Partner@@@@@@@@@@@@@@@@@@@', partner_id)
    #         if partner_id:
    #             # res.update({'address': partner_id})
    #             print("here...............................")
    #             domain = f"[('type', '=', 'delivery'), ('parent_id', '=', {partner_id.id})]"
    #     res = {'domain': {'address': domain}}
    #     print(res,'domain???????????????????')
    #     return res

    # @api.model
    # def _fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     print("i am in side ...............................")
    #     view_id = self.env.ref('change_delivery_address.change_delivery_address_form')
    #     print(view_id, 'View id ,,,,,,,,,,,,,,,,,')
    #     """
    #     Override fields_view_get to set the domain of the address field using the context.
    #     """
    #     res = super(ChangeDeliveryAddress, self)._fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
    #                                                               submenu=submenu)
    #     print(res, '>>>>>>>>>>>>>>>>>>>called')
    #     if view_type == 'form':
    #         if self._context.get('address_domain'):
    #             doc = etree.XML(res['arch'])
    #             for node in doc.xpath("//field[@name='address']"):
    #                 node.set('domain', str(self._context['address_domain']))
    #             res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res

    # @api.depends_context('active_id')
    # @api.model
    # def _compute_customer(self):
    #     print('hi............................')
    #     print(self.env.context,'context!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #     if self.env.context.get('order_id'):
    #         self.partner_id = self.env['sale.order'].browse(self.env.context.get('order_id')).partner_id.id
    # @api.model
    # def find_contact(self, name='', domain=None, operator='ilike', limit=None, order=None):
    #     domain = domain or []
    #     print("hello.........search?????")
    #     order_id = self.env['sale.order'].browse(self.env.context['params']['id'])
    #     domain += [('parent_id', '=', order_id.partner_id.id), ('type', '=', 'delivery')]
    #     print(domain, 'dddddddddddddddddddddddddddomain')
    #     return self._name_search(name, domain, operator, limit, order)
