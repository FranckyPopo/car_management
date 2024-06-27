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
        Car = self.env["car_management.car"]
        instance_car = Car.browse(self.env.context.get('active_id'))
        instance_car.employe_id = self.employe_id
        return True


