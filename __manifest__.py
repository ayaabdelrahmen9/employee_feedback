# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Employee Feedback',
    'author': 'Aya',
    'category': '',
    'version': '17.0.0.1.0',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_feedback.xml',
    ],
    'application': True,
    # 'summary': '',
    # 'sequence': 10,
    # 'description': """ """,
    # 'website': '',
    # 'demo': [],
    # 'installable': True,
    # 'post_init_hook': '',
    # 'license': 'LGPL-3',
}
