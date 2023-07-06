from odoo import models, fields, api

class majors_module(models.Model):
    _name = 'major.model'
    name= fields.Char(string='Name')
    code = fields.Char(string='Code')

    _sql_constraints = [
        (
            'major_code_unique','UNIQUE(code)','ko dc trung'
        )
    ]