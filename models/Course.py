# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
	_name = 'course.model'


	tittle = fields.Char("Titulo", required=True)
	description = fields.Text("Descripcion", required=True)
