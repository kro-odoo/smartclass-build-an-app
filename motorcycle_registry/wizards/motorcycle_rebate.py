# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class MotorcycleRebate(models.TransientModel):
    _name = 'motorcycle.rebate'
    _description = 'Motorcycle Rebate'

    rebate = fields.Float('Apply Rebate')
    # sale_order_id = fields.Many2one('sale.order', string='Sales Order')


    def action_apply_rebate(self):
        active_id = self._context.get('active_id')
        sale_order = self.env['sale.order'].search([('id', '=', active_id)])
        sale_order_products = sale_order.order_line.mapped('product_template_id')
        if any(product.is_motorcycle for product in sale_order_products):
            test = self.env['product.template'].create({         
                    'name': 'Rebate',
                    'uom_id': self.env.ref('uom.product_uom_unit').id,
                    'list_price': self.rebate * sale_order.amount_total,
                })
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_template_id': test.id,
                'name': "Rebate for first purchase",
                'price_unit': -(test.list_price),
            })
