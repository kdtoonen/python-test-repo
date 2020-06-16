import pytest


@pytest.mark.unittest
def test_initial(client):
    rv = client.get('/')
    assert b'The easiest way to make reservations' in rv.data
