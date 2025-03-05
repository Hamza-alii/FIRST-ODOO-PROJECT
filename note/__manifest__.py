{
    'name': 'Note Management',
    'version': '1.0',
    'summary': 'Module for managing notes',
    'category': 'Productivity',
    'author': 'Mr Ali',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv', 
        'views/note_views.xml',
        'data/note_redirect.xml', 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
