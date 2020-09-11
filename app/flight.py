from model import Flight
from model import db
from datetime import datetime


def create_flight(air_field_id, destination, date_time_departure, date_time_arrival):
    new_flight = Flight(air_field=air_field_id,
                        destination=destination,
                        date_time_departure=datetime.strptime(date_time_departure, "%Y-%m-%d %H:%M:%S"),
                        date_time_arrival=datetime.strptime(date_time_arrival, "%Y-%m-%d %H:%M:%S"))

    db.session.add(new_flight)
    db.session.commit()
    return new_flight.id


