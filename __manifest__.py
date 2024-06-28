# -*- coding: utf-8 -*-
{
    'name': "Car management",

    'summary': "Application management",

    'description': """
        Cette application permet de gérer un garrage
    """,

    'author': "Afri Kreto Franck",
    'website': "https://www.akfa.com",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'wizard/car_management_car_wizard.xml',

        'views/car_management_menu.xml',
        'views/car_management_travel.xml',
        'views/car_management_ticket.xml',
        'views/car_management_car.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}

