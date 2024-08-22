# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
import re
from datetime import date




class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    # _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    # _description = "Sales Order"
    # _order = 'date_order desc, id desc'
    # _check_company_auto = True



    # #=== FIELDS ===#


    description = fields.Text(string="Description")
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    certificate_title = fields.Binary(string="Title")
    current_mileage = fields.Float()
    date_registry = fields.Date()
    license_plate = fields.Char()
    registry_number = fields.Char()
    vehicle_image = fields.Image(max_width=1024, max_height=1024)
    
    # computed  vin from following fields
    make = fields.Char()
    model = fields.Char()
    year = fields.Integer()
    serial_number = fields.Char()

    vin = fields.Char(compute="_compute_vin", store=True)
    
    #compute
    @api.depends('make', 'model', 'year', 'serial_number')
    def _compute_vin(self):
        for record in self:
            if all([record.make, record.model, record.year, record.serial_number]):
                record.vin = f"{record.make[:2]}{record.model[:2]}{str(record.year)[:2]}{str(record.serial_number)[:5]}"
            else:
                record.vin = False

    # inverse

    penalty = fields.Float(string='Penalty')
    vin_fees = fields.Float(string='VIN Fees')
    total_fees = fields.Float(compute="_compute_total_fees", inverse="_inverse_total_fees")

    @api.depends('vin_fees', 'penalty')
    def _compute_total_fees(self):
        for record in self:
            record.total_fees = record.vin_fees + record.penalty

    def _inverse_total_fees(self):
        for record in self:
            if record.total_fees is not False:
                # Assume penalty should be 20% of total_fees
                desired_penalty = record.total_fees * 0.20
                # Adjust vin_fees to match the total_fees and desired penalty
                record.penalty = desired_penalty
                record.vin_fees = record.total_fees - record.penalty
            else:
                record.penalty = 0.0
                record.vin_fees = 0.0

    
    # # add reserve field
    # active = fields.Boolean() # at this point they will define the filter but records will be invisible because default active=false
    active = fields.Boolean(default="True") 

    # #relational fields
    # # many2one
    owner_id = fields.Many2one('res.partner')

    # #related fields
    email = fields.Char(related='owner_id.email')
    phone = fields.Char(related='owner_id.phone')
    

    # # m2m
    tag_ids = fields.Many2many('motorcycle.tags')
    
    # o2m
    onwership_transfer_ids = fields.One2many('ownership.transfer', 'registry_id')

    # sql constraints
    _sql_constraints = [('unique_vin', "unique(VIN)", "A VIN with the same name and applicability already exists in this registry.")]


    #  Python Constraints
    @api.constrains('license_plate')
    def _check_license_plate_number(self):
    #check for The license plate -> should follow the following pattern
    
    # To validate an Indian vehicle license number in Odoo using a regex constraint, you can use the following regular expression. Indian license plates typically follow the format:
    
    # Two letters for the state code (e.g., "KA" for Karnataka)
    # Two digits for the district code
    # One or two letters for the series
    # Four digits for the number
    # Example license format: KA01AB1234

        pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$')

        for record in self:
            # Check if license_plate is a string and match the pattern
            if record.license_plate and not pattern.match(record.license_plate):
                raise ValidationError(_("Invalid License Number!"))

    
    # Python Inheritance
    is_verified = fields.Boolean()

    def unlink(self):
        for record in self:
            if record.is_verified:
                raise UserError(_("You cannot delete a verified registry"))
        return super().unlink()

