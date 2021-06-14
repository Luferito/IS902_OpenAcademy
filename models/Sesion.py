# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sesion(models.Model):
    _name = 'sesion.model'
    _description = "Sesiones OpenAcademy"

    nombre = fields.Char("Titulo",required=True)
    fecha = fields.Date("Fecha de inicio", required=True)
    duracion = fields.Integer("Duración en minutos", required=True)
    asientos = fields.Integer("Cantidad de asientos", required=True)
    instructor = fields.Many2one("res.partner", "Instructor", required=True, 
        domain=['|', ('instructor', '=', True), ('category_id.name','ilike',"Teacher")])
    curso = fields.Many2one("course.model", "Curso", required=True)
    asistentes = fields.Many2many("res.partner", string="Asistentes",
        domain=['|', ('instructor', '=', False), '&', ('category_id.name', 'not ilike', "Teacher"), ('instructor', '=', False)])
    porcentaje_asientos_ocupados = fields.Float("Asientos ocupados", compute='_compute_asientos_ocupados', readonly=True)

    @api.depends('asistentes')
    def _compute_asientos_ocupados(self):
        for record in self:
            record.porcentaje_asientos_ocupados = len(record.asistentes) / record.asientos * 100