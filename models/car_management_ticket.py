from odoo import models, fields


class Ticket(models.Model):
    _name = 'car_management.ticket'
    _description = "Representation d'un Ticket"

    contact_id = fields.Many2one(
        "res.partner",
        string="Nom du client",
        required=True,
    )
    amount = fields.Float(string="Montant", required=True)
    destionation = fields.Char(string="Destination", required=True)
    car_id = fields.Many2one(
        "car_management.car",
        string="Voiture",
        required=True,
    )
    date_departure = fields.Datetime(
        required=True,
        string="Date de départ",
        default=fields.Datetime.now(),
    )
    date = fields.Datetime(
        required=True,
        string="Date",
        default=fields.Datetime.now(),
    )

    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.contact_id.name}({order.car_id.car_model})"
