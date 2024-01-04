{
    'name': 'estate',
    'version': '2.0',
    'author': 'Harry',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_setting_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
        
    ],
    'demo': [
        'demo/estate_demo.xml',
    ],
    'installable': True,
    'application': True,
}
