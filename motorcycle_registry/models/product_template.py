# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_motorcycle = fields.Boolean(help="Motorcycle")
    is_rebate = fields.Boolean()
    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Selection([
            ('os', 'Small'),
            ('om', 'Medium'),
            ('ol', 'Large'),
            ('xl', 'Extra Large')
        ])
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    launch_date = fields.Date()

