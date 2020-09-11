from model import AirField
from model import db


def create_air_field(air_field_name):
    new_airfield = AirField(air_field=air_field_name)
    db.session.add(new_airfield)
    db.session.commit()
    return new_airfield.id



