{
    'name': 'Developers management addon',
    'author': 'tahomi',
    'category': 'Uncategorized',
    'summary': "",
    'description': "",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/developer_view.xml',
        'views/company_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'OEEL-1',
}