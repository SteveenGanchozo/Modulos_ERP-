# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCapacitar(http.Controller):
#     @http.route('/modulo_capacitar/modulo_capacitar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_capacitar/modulo_capacitar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_capacitar.listing', {
#             'root': '/modulo_capacitar/modulo_capacitar',
#             'objects': http.request.env['modulo_capacitar.modulo_capacitar'].search([]),
#         })

#     @http.route('/modulo_capacitar/modulo_capacitar/objects/<model("modulo_capacitar.modulo_capacitar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_capacitar.object', {
#             'object': obj
#         })
