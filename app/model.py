from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(200), nullable=False)
    reset_code = db.Column(db.String(200), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    air_field = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(240), nullable=True)
    date_time_departure = db.Column(db.DateTime, nullable=False)
    date_time_arrival = db.Column(db.DateTime, nullable=False)


class AirField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    air_field = db.Column(db.String(200), nullable=False)


class SeatsAvailable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(20), nullable=False)
    number_of_seats = db.Column(db.Integer, nullable=False)
    flight_id = db.Column(db.Integer, nullable=False)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    reserved_class = db.Column(db.String(16), nullable=False)
    passenger_first_name = db.Column(db.String(40), nullable=False)
    passenger_last_name = db.Column(db.String(40), nullable=False)