# -*- coding: utf-8 -*-
{
    'name': 'Embed Videos',
    'version': '1.0',
    'website': 'https://erplabz.com',
    'author': 'ERP Labz',
    
    'category': 'Extra Tools',
    'summary': 'Embed Videos',
    'description': """this module embed youtube video within odoo form with given video url
""",
    'depends': ['base'],
    'data': [
	    'data/data.xml',
            'views/video_links.xml',
            'wizard/watch_video_view.xml',
        
    ],
	'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
