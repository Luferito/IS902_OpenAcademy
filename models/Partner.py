# -*- coding: utf-8 -*-

from odoo import models, fields

class Partner(models.Model):
    _inherit  = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)
    sesiones = fields.Many2many('sesion.model', string="Sesiones matriculadas", readonly=True)