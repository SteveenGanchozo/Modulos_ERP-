# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloEquipo(http.Controller):
#     @http.route('/modulo_equipo/modulo_equipo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_equipo/modulo_equipo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_equipo.listing', {
#             'root': '/modulo_equipo/modulo_equipo',
#             'objects': http.request.env['modulo_equipo.modulo_equipo'].search([]),
#         })

#     @http.route('/modulo_equipo/modulo_equipo/objects/<model("modulo_equipo.modulo_equipo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_equipo.object', {
#             'object': obj
#         })
