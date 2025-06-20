{
    'name': 'Sale Order Customization',
    'version': '1.0',
    'summary': 'Personalización de prendas tras venta o presupuesto',
    'description': 'Permite al cliente subir logo y definir personalización tras la venta.',
    'author': 'Serial Printer + ChatGPT',
    'depends': ['sale', 'sale_management', 'mail', 'portal'],
    'data': [
        'views/sale_order_customization_views.xml',
    ],
    'installable': True,
    'application': False,
}