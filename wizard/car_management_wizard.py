from odoo import api, fields, models

class Wizard(models.TransientModel):
    _name = 'car_management.wizard'
    _description = 'CarManagement Wizard'

    employe_id = fields.Many2one(
        "hr.employee",
        required=True,
        string="Chauffeur",
    )

    def valid(self):
        print("--------------------- button click")
        pass
