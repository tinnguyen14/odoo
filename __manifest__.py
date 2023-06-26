# -*- coding: utf-8 -*-
{
    'name': "discipline",

    'summary': """Quy trình xử lý học vụ của sinh viên dành cho 1 khoa hoặc nhiều khoa""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Odoo core/odoo core',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/major_view.xml',
    ],
    # only loaded in demonstration mode
    "application": True
}
