from odoo import fields, models


class PrefEmployee(models.Model):
    _inherit = 'hr.employee'

    preference = fields.Many2one("hr.employee.preference.music", "Music preference", store=True, readonly=False)
