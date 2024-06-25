# -*- coding: utf-8 -*-
# from odoo import http


# class CarManagement(http.Controller):
#     @http.route('/car_management/car_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_management/car_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_management.listing', {
#             'root': '/car_management/car_management',
#             'objects': http.request.env['car_management.car_management'].search([]),
#         })

#     @http.route('/car_management/car_management/objects/<model("car_management.car_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_management.object', {
#             'object': obj
#         })

