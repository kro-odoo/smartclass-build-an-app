# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _

class MotorcycleTags(models.Model):
    _name = 'motorcycle.tags'
    _description = 'Motorcycle Tags'

    name = fields.Char()


