from flask import Blueprint, request, Response
import airfield
import flight
import reservation
services = Blueprint('services', __name__, template_folder='templates')


@services.route('/flight', methods=(['POST']))
def flight_handler():
    if request.json:
        air_field_id = request.json['air_field_id']
        destination = request.json['destination']
        date_time_departure = request.json['date_time_departure']
        date_time_arrival = request.json['date_time_arrival']
        flight_id = flight.create_flight(air_field_id,
                                         destination,
                                         date_time_departure,
                                         date_time_arrival)
        # TODO repetitive code, put into a function
        return Response('{"Status": "Created", "id": "' + str(flight_id) + '"}', status=201,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Bad request'}", status=400, mimetype='application/json')


@services.route('/airfield', methods=(['POST']))
def air_field_handler():
    if request.json:
        air_field = request.json['air_field']
        air_field_id = airfield.create_air_field(air_field)
        return Response('{"Status": "Created", "id": "' + str(air_field_id) + '"}', status=201,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Bad request'}", status=400, mimetype='application/json')


@services.route('/reservation', methods=(['POST']))
def reservation_handler():
    if request.json:
        flight_id = request.json['flight_id']
        user_id = request.json['user_id']
        reserved_class = request.json['reserved_class']
        passenger_first_name = request.json['passenger_first_name']
        passenger_last_name = request.json['passenger_last_name']
        reservation_id = reservation.create_reservation(flight_id, user_id, reserved_class, passenger_first_name, passenger_last_name)
        return Response('{"Status": "Created", "id": "' + str(reservation_id) + '"}', status=201,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Bad request'}", status=400, mimetype='application/json')
