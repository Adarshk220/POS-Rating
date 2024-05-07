{
    'name': 'POS Rating',
    'author': 'Adarsh',
    'version': '17.0.1.0.0',
    'summary': 'POS Rating',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/product_product_views.xml'
    ],
    'sequence': -110,
    'application': True,
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_rating/static/xml/pos_list.xml',
            'pos_rating/static/src/js/pos_rating.js',
            'pos_rating/static/xml/pos_screen.xml',
            'pos_rating/static/src/js/pos_rating_order_line.js',
            'pos_rating/static/xml/pos_order_line.xml',
        ],
    },
}
