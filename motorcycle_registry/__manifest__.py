# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Motorcycle Registry',
    'version': '1.0',
    'category': 'Kawiil/Custom Modules',
    'summary': 'Manage Registration of Motorcycles',
    'description': """
Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycle of the brand.
    """,
    'depends': ['product', 'sale_management'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_registry_menu.xml',
        'views/motorcycle_registry_views.xml',
        'views/motorcycle_tags_views.xml',
        'views/product_template_views.xml',
        'wizards/motorycycle_rebate_views.xml',
        'views/sale_order_views.xml',
        'reports/motorcycle_registry_report.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml'
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
