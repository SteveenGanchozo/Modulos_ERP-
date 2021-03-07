# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloDescripción(http.Controller):
#     @http.route('/modulo_descripción/modulo_descripción/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_descripción/modulo_descripción/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_descripción.listing', {
#             'root': '/modulo_descripción/modulo_descripción',
#             'objects': http.request.env['modulo_descripción.modulo_descripción'].search([]),
#         })

#     @http.route('/modulo_descripción/modulo_descripción/objects/<model("modulo_descripción.modulo_descripción"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_descripción.object', {
#             'object': obj
#         })
