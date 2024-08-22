from odoo import http

class MotorcycleRegistry(http.Controller):

    @http.route('/compare', auth='public', website=True)
    def motorcycle_compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('is_motorcycle', '=', True)])
        values = {
            'products': motorcycles
        }
        return http.request.render('motorcycle_website.motorcycle_compare', values)


