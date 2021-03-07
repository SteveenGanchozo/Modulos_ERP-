# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloMigración(http.Controller):
#     @http.route('/modulo_migración/modulo_migración/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_migración/modulo_migración/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_migración.listing', {
#             'root': '/modulo_migración/modulo_migración',
#             'objects': http.request.env['modulo_migración.modulo_migración'].search([]),
#         })

#     @http.route('/modulo_migración/modulo_migración/objects/<model("modulo_migración.modulo_migración"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_migración.object', {
#             'object': obj
#         })
