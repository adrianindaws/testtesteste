# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea1Indaws(http.Controller):
#     @http.route('/tarea1_indaws/tarea1_indaws/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea1_indaws/tarea1_indaws/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea1_indaws.listing', {
#             'root': '/tarea1_indaws/tarea1_indaws',
#             'objects': http.request.env['tarea1_indaws.tarea1_indaws'].search([]),
#         })

#     @http.route('/tarea1_indaws/tarea1_indaws/objects/<model("tarea1_indaws.tarea1_indaws"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea1_indaws.object', {
#             'object': obj
#         })
