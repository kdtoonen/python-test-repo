from model import Reservation
from model import db
from model import Flight
from model import AirField


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
    list_of_reservations = Reservation.query\
        .join(Flight, Reservation.flight_id == Flight.id)\
        .join(AirField, Flight.air_field == AirField.id)\
        .add_columns(Reservation.id,
                     Reservation.passenger_first_name,
                     Reservation.passenger_last_name,
                     Reservation.reserved_class,
                     Flight.date_time_arrival,
                     Flight.date_time_departure,
                     Flight.destination,
                     AirField.air_field)\
        .filter(Reservation.user_id == user_id)\
        .order_by(Flight.date_time_departure.asc())
    return list_of_reservations


def delete_reservation(reservation_id):
    reservation = Reservation.query.filter(Reservation.id == reservation_id).first()
    print(str(reservation.passenger_first_name))
    db.session.delete(reservation)
    db.session.commit()
    pass




