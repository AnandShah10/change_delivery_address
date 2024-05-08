# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'change_delivery_address',
    'version': '1.0',
    'summary': "Change Delevery address module",
    'sequence': 10,
    'author': "anand",
    'description': """
Help user to change the delivery address for the contact by using a button
""",
    'category': 'Custom/Conatct',
    'website': 'https://www.odoo.com/',
    'depends': ['mail', 'contacts','sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/address.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
