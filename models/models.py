# -*- coding: utf-8 -*-

from odoo import models, fields, api


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


class Travel(models.Model):
    _name = "car_management.travel"
    _description = "Representation d'un voyage"

    car_id = fields.Many2one(
        "car_management.car",
        string="Voiture",
    )
    departure_location = fields.Char(string="Lieu départ")
    destination = fields.Char(string="Destination")
    date_departure = fields.Datetime(string="Date de départ")
    date_arrival = fields.Datetime(string="Date d'arrivée")
    travel_time = fields.Integer(string="Travel time", inverse="_inverse_travel_time")
    numbers_of_places = fields.Integer(string="Nombre de place")

    def _inverse_travel_time(self):
        for record in self:
            record.travel_time = record.travel_time * 2

    @api.onchange("car_id")
    def _onchange_car_id(self):
        self.numbers_of_places = self.car_id.numbers_of_places


class Ticket(models.Model):
    _name = 'car_management.ticket'
    _description = "Representation d'un Ticket"

    contact_id = fields.Many2one(
        "contacts",
        string="Nom du client",
        required=True,
    )
    amount = fields.Float(string="Monatant", required=True)
    destionation = fields.Char(string="Destination", required=True)
    car_id = fields.Many2one(
        "car_management.car",
        string="Voiture",
        required=True,
    )
    date_departure = fields.Datetime(required=True)
    date = fields.Datetime(required=True)


