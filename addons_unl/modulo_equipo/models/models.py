# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Equipo(models.Model):
    _name = 'reg.equipo'
    _description = 'Descripció de los equipos de computación'

    computador = fields.Char(string="Computador")
    procesador = fields.Char(string="Procesador")
    s_operativo = fields.Char(string="Sistema Operativo")
    ram = fields.Integer(string="RAM")
    fabricante = fields.Char(string="Fabricante")
    modelo = fields.Char(string="Modelo")
    descripcion= fields.Many2many('reg.descripcion',
                                    relation='reg_descripcion_rel',
                                    column1='des_id', 
                                    column2='eq_id', 
                                    string='Descripcion')
    eq_migrado = fields.Selection([('si', 'Si'),('no', 'No')],  default='no')
    migrable = fields.Selection([('si', 'Si'),('no', 'No')],  default='si')
  