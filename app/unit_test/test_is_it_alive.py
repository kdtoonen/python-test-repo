import pytest


@pytest.mark.unittest
def test_initial(client):
    rv = client.get('/')
    assert b'Fly me to the moon' in rv.data
