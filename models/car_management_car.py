from odoo import models, fields


class Car(models.Model):
    _name = "car_management.car"
    _description = "Representation d'une voiture"

    car_model = fields.Char(string="Modèle de la voiture", requied=True)
    manufacturer = fields.Selection(
        string="Fabriquant",
        selection=[
            ("toyota", "Toyota"),
            ("ford", "Ford"),
            ("honda", "Honda"),
            ("chevrolet", "Chevrolet"),
            ("bmx", "BMW"),
            ("mercedes-benz", "Mercedes-Benz"),
            ("audi", "Audi"),
            ("volkswagen", "Volkswagen"),
            ("nissan", "Nissan"),
            ("kia", "Kia"),
            ("subaru", "Subaru"),
            ("volvo", "Volvo"),
            ("lexus", "Lexus"),
            ("tesla", "Tesla"),
            ("jaguar", "Jaguar"),
            ("land rover", "Land Rover"),
            ("porsche", "Porsche"),
            ("mazda", "Mazda"),
            ("fiat", "Fiat"),
        ],
        required=True,
    )
    numbers_of_places = fields.Selection(
        string="Nombre de place",
        required=True,
        default="4",
        selection=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
        ]
    )
    fuel_type = fields.Selection(
        string="Type de carburant",
        required=True,
        default="essence",
        selection=[
            ("essence", "Essence"),
            ("diesel", "Diesel"),
            ("ethanol", "Éthanol"),
            ("gpl", "GPL (Gaz de Pétrole Liquéfié)"),
            ("hydrogène", "Hydrogène"),
            ("electricité", "Électricité"),
            ("hybride", "Hybride (électricité + essence ou diesel) "),
        ]
    )
    employe_id = fields.Many2one(
        "hr.employee",
        required=True,
        string="Chauffeur",
    )

    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.manufacturer}({order.car_model})".title()

    def driver_details(self):

        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.employee",
            "views": [[False, "form"]],
            "res_id": self.employe_id.id,
            "target": "new",
        }
