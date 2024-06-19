from odoo.tests import common
from odoo import fields
from odoo.exceptions import AccessError


class TestCompany(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.test_user = self.env['res.users'].create({
            'login': 'test_user',
            'name': 'Test User',
            'email': 'test_user@example.com',
            'password': 'test_password',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])]
        })

    def test_user_access_company(self):
        self.env = self.env(user=self.test_user) 

        comp_record = self.env['developers_management.company'].create({
            'name': 'Test Company',
        })

        companies = self.env['developers_management.company'].search([])
        self.assertTrue(len(companies) > 0)

        with self.assertRaises(AccessError):
            comp_record.write({
                'name': 'New value',
            })

        with self.assertRaises(AccessError):
            comp_record.unlink()
    
    def test_create_developer(self):
        company = self.env['developers_management.company'].create({
            'name': 'Test Company',
            'address': '123 Main St',
        })

        developer = self.env['developers_management.developer'].create({
            'name': 'John Doe',
            'company': company.id,
        })

        comp_devs = company.developers
        self.assertTrue(len(comp_devs) > 0)
