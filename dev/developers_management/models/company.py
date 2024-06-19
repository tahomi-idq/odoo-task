from odoo import fields, models

class Company(models.Model):
    _name = "developers_management.company"

    name = fields.Char('Company name')
    address= fields.Text('Company address')
    developers = fields.One2many('developers_management.developer', inverse_name='company')

    _sql_constraints = [('company_name', 'unique (name)', 'Name must be unique')]
            

