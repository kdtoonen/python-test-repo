from model import Reservation
from model import db


def create_reservation(flight_id, user_id, reserved_class, passenger_first_name, passenger_last_name):
    new_reservation = Reservation(flight_id=flight_id,
                                  user_id=user_id,
                                  reserved_class=reserved_class,
                                  passenger_first_name=passenger_first_name,
                                  passenger_last_name=passenger_last_name)
    db.session.add(new_reservation)
    db.session.commit()
    return new_reservation.id

def get_reservations_for_user(user_id):
    list_of_reservations = Reservation.query.filter_by(user_id=user_id).all()
    return list_of_reservations



