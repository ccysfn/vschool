# -*- coding: utf-8 -*-
from odoo import http

# class Vschool(http.Controller):
#     @http.route('/vschool/vschool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vschool/vschool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vschool.listing', {
#             'root': '/vschool/vschool',
#             'objects': http.request.env['vschool.vschool'].search([]),
#         })

#     @http.route('/vschool/vschool/objects/<model("vschool.vschool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vschool.object', {
#             'object': obj
#         })