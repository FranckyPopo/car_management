from odoo import models, fields, api


class Travel(models.Model):
    _name = "car_management.travel"
    _description = "Representation d'un voyage"

    car_id = fields.Many2one(
        "car_management.car",
        string="Voiture",
    )
    departure_location = fields.Char(string="Lieu de départ")
    destination = fields.Char(string="Destination")
    date_departure = fields.Datetime(string="Date de départ", default=fields.Datetime.now())
    date_arrival = fields.Datetime(string="Date d'arrivée", default=fields.Datetime.now())
    travel_time = fields.Integer(string="Durée du voyage", inverse="_inverse_travel_time", default=1)
    numbers_of_places = fields.Integer(
        string="Nombres de places",
        readonly=True,
        compute="_compute_numbers_of_places"
    )

    def _inverse_travel_time(self):
        for record in self:
            record.travel_time = record.travel_time * 2

    @api.onchange("car_id")
    def _compute_numbers_of_places(self):
        for record in self:
            record.numbers_of_places = record.car_id.numbers_of_places



    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.car_id.car_model}"
