# -*- coding: utf-8 -*-
{
    'name': "Fetch Mail Invoice2data",

    'summary': """

            This modules is used to create vendor invoices via e-mail. It depends on two other modules:
            
            - batch vendor import invoice new
            - yml template module
            
            
    """,
    'description': """
    """,
        'author': "Magnus - DK",
        'website': "http://www.yourcompany.com",
        'category': 'Others',
        'version': '0.1',
        'depends': ['mail','attachment_base_synchronize','fetchmail','operating_unit'],
        'data': ['views/fetchmail_server_view.xml'],
        'demo': [],
    }