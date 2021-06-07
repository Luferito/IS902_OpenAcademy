# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
	_name = 'course.model'
	_description = "IS902 OpenAcademy Module"

	titulo = fields.Char(string="Titulo", required=True)
	descripcion = fields.Text(string="Descripcion", required=True)
