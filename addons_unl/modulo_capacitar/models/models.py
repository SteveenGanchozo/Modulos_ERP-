# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Capacitado(models.Model):
    _name = 'reg.capacitado'
    _description = ''
    
    fecha = fields.Datetime('Fecha', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
    user= fields.Many2many('res.partner', relation='instructor_rel', required=True)
    lista = fields.Many2many('res.partner')
    observaciones = fields.Text()
    
