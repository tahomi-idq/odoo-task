from odoo.tests import common
from odoo import fields
from odoo.exceptions import AccessError


class TestDeveloper(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.test_user = self.env['res.users'].create({
            'login': 'test_user',
            'name': 'Test User',
            'email': 'test_user@example.com',
            'password': 'test_password',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])]
        })

    def test_user_access_developer(self):
        self.env = self.env(user=self.test_user) 

        dev_record = self.env['developers_management.developer'].create({
                'name': 'Test Developer',
        })

        developers = self.env['developers_management.developer'].search([])
        self.assertTrue(len(developers) > 0)

        with self.assertRaises(AccessError):
            dev_record.write({
                'name': 'New value',
            })

        with self.assertRaises(AccessError):
            dev_record.unlink()

    def test_link_company(self):

        developer = self.env['developers_management.developer'].create({
            'name': 'John Doe',
        })

        company = self.env['developers_management.company'].create({
            'name': 'Test Company',
            'address': '123 Main St',
            'developers': [developer.id]
        })

        self.assertEqual(developer.company.id, company.id)
