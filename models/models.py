# -*- coding: utf-8 -*-

from odoo import models, fields, api
from pprint import pprint


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
        string="Chauffeur"
    )

    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.manufacturer}({order.car_model})".title()

    def action_test(self):
        print("employ -----------------------------------------------------")

        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.employee",
            "views": [[False, "form"]],
            "res_id": self.employe_id.id,
            "target": "new",
        }

class Travel(models.Model):
    _name = "car_management.travel"
    _description = "Representation d'un voyage"

    car_id = fields.Many2one(
        "car_management.car",
        string="Voiture",

    )
    departure_location = fields.Char(string="Lieu départ")
    destination = fields.Char(string="Destination")
    date_departure = fields.Datetime(string="Date de départ", default=fields.Datetime.now())
    date_arrival = fields.Datetime(string="Date d'arrivée", default=fields.Datetime.now())
    travel_time = fields.Integer(string="Durée du voyage", inverse="_inverse_travel_time", default=1)
    numbers_of_places = fields.Integer(string="Nombre de place", readonly=True)

    def _inverse_travel_time(self):
        for record in self:
            record.travel_time = record.travel_time * 2

    @api.onchange("car_id")
    def _onchange_car_id(self):
        self.numbers_of_places = self.car_id.numbers_of_places

    def _compute_display_name(self):
        for order in self:
            order.display_name = f"{order.car_id.car_model}"


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
