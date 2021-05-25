# -*- coding: utf-8 -*-
{
    'name': "Custom Printout Reports",
    'version': '1.0.0',
    'author': 'Developer',
    'category': 'Reports',
    'summary': 'Print Module to handle specific Reports',
    'description': """
    Print Module to handle specific Reports Requirement
    """,
    'depends': ['account'],
    'data': [
        'reports/account_invoice.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
