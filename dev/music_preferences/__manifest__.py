{
    'name': 'Music preferences addon',
    'author': 'Tahomi',
    'category': 'Uncategorized',
    'summary': "",
    'description': "",
    'version': '1.0',
    'depends': ['hr', 'base'],
    'data': [
        'views/preferences_view.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'OEEL-1',
}