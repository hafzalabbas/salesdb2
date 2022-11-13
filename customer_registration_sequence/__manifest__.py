# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Registration Sequence',
    'version': '16.0.0.1',
    'category':'All',
    'license':'OPL-1',
    'summary': 'This module allow to create automatic sequence of partner',
    'description':""" This module generate customer registration code.""",
    'author': 'Odoo Coders',
    'website': 'https://www.odoocoders.com',
    'depends':['base'],
    'data':[
        'data/partner_ir_sequence_data.xml',
        'views/partner_reg_index.xml',
        ],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.gif'],
}
