# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sesion(models.Model):
    _name = 'sesion.model'
    _description = "Sesiones OpenAcademy"

    nombre = fields.Char("Titulo",required=True)
    fecha = fields.Date("Fecha de inicio", required=True)
    duracion = fields.Integer("Duración en minutos", required=True)
    asientos = fields.Integer("Cantidad de asientos", required=True)
    instructor = fields.Many2one("res.partner", "Instructor", required=True)
    curso = fields.Many2one("course.model", "Curso", required=True)
    asistentes = fields.Many2many("res.partner", string="Asistentes")