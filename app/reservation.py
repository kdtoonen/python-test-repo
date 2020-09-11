from model import Reservation
from model import db


def create_reservation(flight_id, user_id, reserved_class):
    new_reservation = Reservation(flight_id=flight_id,
                                  user_id=user_id,
                                  reserved_class=reserved_class)
    db.session.add(new_reservation)
    db.session.commit()
    return new_reservation.id



