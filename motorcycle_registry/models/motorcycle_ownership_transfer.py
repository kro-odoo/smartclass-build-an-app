# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class OwnershipTransfer(models.Model):
    _name = 'ownership.transfer'
    _description = 'Ownership Transfer'

    registry_id = fields.Many2one('motorcycle.registry', string="Motorcycle Registry", required=True)
    transfer_date = fields.Date(string="Transfer Date", required=True)
    previous_owner = fields.Many2one('res.partner', string="Previous Owner", required=True)
    new_owner = fields.Many2one('res.partner', string="New Owner", required=True)
