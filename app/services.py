from flask import Blueprint, request, Response
import airfield
import flight
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

        return Response('{"Status": "Created", "id": "' + str(flight_id) + '"}', status=201,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Fail'}", status= 404, mimetype='application/json')


@services.route('/airfield', methods=(['POST']))
def air_field_handler():
    if request.json:
        air_field = request.json['air_field']
        air_field_id = airfield.create_air_field(air_field)
        return Response('{"Status": "Created", "id": "' + str(air_field_id) + '"}', status=201,
                        mimetype='application/json')
    else:
        return Response("{'Status': 'Fail'}", status= 404, mimetype='application/json')


