# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
	_name = 'course.model'


	tittle = fields.Char(string="Titulo", required=True)
	description = fields.Text(string="Descripcion", required=True)
