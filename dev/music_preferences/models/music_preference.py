from odoo import fields, models


class MusicPreference(models.Model):
    _name = 'hr.employee.preference.music'

    name = fields.Char(string="Name", required=True)
