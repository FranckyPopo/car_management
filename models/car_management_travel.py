from odoo import models, fields, api
from pprint import pprint


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
    travel_time = fields.Char(string="Durée du voyage", compute="_compute_travel_time")
    numbers_of_places = fields.Integer(
        string="Nombres de places",
        readonly=True,
        compute="_compute_numbers_of_places",
    )

    @api.depends("car_id")
    def _compute_numbers_of_places(self):
        for record in self:
            record.numbers_of_places = record.car_id.numbers_of_places

    @api.depends("date_departure", "date_arrival")
    def _compute_travel_time(self):

        for record in self:
            calcule_travel_time = record.date_arrival - record.date_departure
            travel_time = ""

            if calcule_travel_time.days :
                travel_time = f"{calcule_travel_time.days} jour(s)"

            if calcule_travel_time.seconds:
                total_minutes = calcule_travel_time.seconds // 60

                # Calcule des heure(s) et minute(s)
                if total_minutes:
                    total_hours = total_minutes // 60

                    if total_hours > 0:
                        print("Oui 1")
                        travel_time = travel_time + f" {total_hours} heure(s)"

                    # Heures et minutes restante
                    remaining_time = total_minutes % 60
                    remaining_minute = remaining_time % 60

                    if remaining_time and travel_time:
                        travel_time = f"{travel_time} et {remaining_minute} minute(s)"

                    if remaining_minute and not travel_time:
                        travel_time = f"{remaining_minute} minute(s)"

            record.travel_time = f"{travel_time}"


    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.car_id.car_model}"


