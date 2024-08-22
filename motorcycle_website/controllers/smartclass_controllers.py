from odoo import http
from odoo.http import request

class Mycontroller(http.Controller):
    # @http.route('/my/website/page', type='http', auth='public')
    # def my_controller_method(self, **kw):
    #     # return "Hello, odoo17!"
    #     data = request.env['res.partner'].search([])
    #     values = {
    #         'partners' : data 
    #     }
    #     return request.render('motorcycle_website.get_partners', values)
    
    @http.route('/get/data', type='http', auth='public')
    def get_data(self):
        data = request.env['res.partner'].search_read([])
        values = {
            'partners': data
        }
        # return {'partners': data}
        return request.render('motorcycle_website.get_partners', values)