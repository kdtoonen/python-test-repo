import pytest


@pytest.mark.unittest
def test_create_reservation(client, mocker):
    mocker.patch('reservation.create_reservation', return_value=1)
    rv = client.post('/reservation', json={"flight_id": 2, "user_id": 1, "reserved_class": "business",
                                           "passenger_first_name": "Bruce", "passenger_last_name": "Banner"})
    json_data = rv.get_json()
    assert json_data["Status"] == 'Created'
    assert rv.status_code == 201


@pytest.mark.unittest
def test_create_reservation_invalid_json(client, mocker):
    mocker.patch('reservation.create_reservation', return_value=1)
    rv = client.post('/reservation', data=dict(e_mail='test@test.com', first_name='test', last_name='test'))
    print(str(rv))
    json_data = rv.get_json()
    assert json_data["Status"] == 'Bad request'
    assert rv.status_code == 400


@pytest.mark.unittest
def test_create_reservation_method_not_allowed(client, mocker):
    mocker.patch('reservation.create_reservation', return_value=1)
    rv = client.delete('/reservation')
    assert rv.status_code == 405
