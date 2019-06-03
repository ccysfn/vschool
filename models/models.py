# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'
    grade = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class student(models.Model):
    _name = 'vschool.student'
    _inherits = {'res.partner','partner_id'}
    ddd = fields.Char()