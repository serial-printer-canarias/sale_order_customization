from odoo import models, fields

class SaleOrderLineCustomization(models.Model):
    _name = 'sale.order.line.customization'
    _description = 'Personalización de línea de pedido'

    order_line_id = fields.Many2one('sale.order.line', string='Línea de pedido', ondelete='cascade', required=True)
    logo_file = fields.Binary('Logo a imprimir')
    logo_filename = fields.Char('Nombre de logo')
    personalization_method = fields.Selection([
        ('serigrafia', 'Serigrafía'),
        ('bordado', 'Bordado'),
        ('dtf', 'DTF'),
        ('ninguna', 'Ninguna'),
    ], string='Tipo de personalización', required=True, default='ninguna')
    print_color = fields.Selection([
        ('white', 'Blanco'),
        ('black', 'Negro'),
        ('red', 'Rojo'),
        # Añade aquí el resto de los 47 colores NS300
    ], string="Color impresión")
    print_size = fields.Selection([
        ('peq', 'Pequeño (10x10)'),
        ('med', 'Mediano (20x20)'),
        ('gra', 'Grande (30x30)'),
    ], string="Tamaño impresión")
    print_position = fields.Selection([
        ('front', 'Frontal'),
        ('back', 'Espalda'),
        ('sleeve_left', 'Manga Izquierda'),
        ('sleeve_right', 'Manga Derecha'),
    ], string="Posición")
    preview_image = fields.Binary('Mockup generado')
    notes = fields.Text('Notas adicionales')