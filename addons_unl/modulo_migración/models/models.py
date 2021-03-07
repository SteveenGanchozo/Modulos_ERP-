# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Migración(models.Model):
    _name = 'reg.migracion'
    _description = ''

    titulo= fields.Text()
    fecha = fields.Datetime('Fecha', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
    equipo = fields.Many2many('reg.equipo')
    observaciones = fields.Text()
    eq_migrado = fields.Selection([('0', '0%'),('5', '5%'),('25', '25%'),('50', '50%'),('75', '75%'),('100', '100%')], default='0')
    respaldo_info = fields.Selection([('si', 'Si'),('no', 'No')])
    migrable = fields.Selection([('si', 'Si'),('no', 'No')])
    fechaSoftware = fields.Date('Fecha', required=False, readonly=False, select=True)
    user= fields.Many2many('res.partner', relation='tecnico_rel', required=True)