from odoo import models, fields, api

class classes_module(models.Model):
    _name = 'classes.model'
    name= fields.Char(string='Name')
    code = fields.Char(string='Code')
    major_id = fields.Many2one('major.model', string='Major')
    teacher_id = fields.Many2one(comodel_name='res.users', string='Teacher')

