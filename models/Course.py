# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
	_name = 'course.model'
	_description = "Cursos OpenAcademy"

	name = fields.Char(string="Titulo", required=True)
	description = fields.Text(string="Descripción", required=True)
