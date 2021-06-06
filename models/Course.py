# -*- coding: utf-8 -*-

 from odoo import models, fields, api

 class Course(models.Model):
     _name = 'Course.model'

     tittle = fields.Char()
     description = fields.Text()
