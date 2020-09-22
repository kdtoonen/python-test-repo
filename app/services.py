from flask import Blueprint, request, Response
import airfield
import flight
import reservation
import datetime
import json
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
    if request.method == 'POST':
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

    else:
        return Response("{'Status': 'Method not allowed'}", status=405, mimetype='application/json')


@services.route('/reservation/id/<int:reservation_id>', methods=(['DELETE']))
def reservation_delete_handler(reservation_id):
    if request.method == 'DELETE':
        reservation.delete_reservation(reservation_id)
        return Response('{"Status": "Deleted", "id": "' + str(reservation_id) + '"}', status=202,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Method not allowed'}", status=405, mimetype='application/json')


@services.route('/reservations/userid/<int:user_id>', methods=(['GET']))
def reservation_get_handler(user_id):
    if request.method == 'GET':
        list_of_reservations = reservation.get_reservations_for_user(user_id)
        reservation_items = []
        if list_of_reservations:
            for reservation_item in list_of_reservations:
                date_time_departure = reservation_item.date_time_departure
                reservation_items.append([reservation_item.id,
                                          reservation_item.passenger_first_name,
                                          reservation_item.passenger_last_name,
                                          date_time_departure.strftime('%m-%d-%Y %H:%M:%S'),
                                          reservation_item.destination,
                                          reservation_item.air_field,
                                          reservation_item.reserved_class])
            return make_service_response(202, 'OK', '"Reservations": "' + json.dumps(reservation_items) + '"')
        else:
            return make_service_response(202, 'OK', '')
    else:
        return make_service_response(405, 'Method not allowed', '')


def make_service_response(status_code, status_message, content):
    content_message = ''
    if content:
        content_message = ", " + content
    return Response("{'Status': '" + status_message + content_message + "'}", status=status_code, mimetype='application/json')
