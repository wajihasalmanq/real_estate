# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate',
    'author': 'Wajiha Salman',
    'category': 'Real Estate',
    'version': '16.0',
    'summary': ' Estate',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base'],
    'data': [
        # "data/estate_property_data.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml"
    ],
    'application': True,
    'license': 'LGPL-3',
}
