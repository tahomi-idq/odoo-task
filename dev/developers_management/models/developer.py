from odoo import models, fields, api

class Developer(models.Model):
    _name = 'developers_management.developer'

    name = fields.Char('Name', required=True)
    type = fields.Selection(string='Developer employment type', selection=[
        ('front-end', 'Front-end'), 
        ('backend', 'Backend'), 
        ('fullstack', 'Fullstack'), 
        ('out-stuff', 'Out stuff')
    ])
    global_identification = fields.Char('Global identification',compute='_compute_global_identification', store=True)
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    address = fields.Text('Address')
    date_of_birth = fields.Date('Date of birth')
    position = fields.Char('Position')
    company = fields.Many2one(comodel_name='developers_management.company', string='Company', ondelete='restrict')

    _sql_constraints = [('developer_name', 'unique (name)', 'Name must be unique')]

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for rec in self:
            rec.global_identification = f'{rec.name}-{rec.type}'
