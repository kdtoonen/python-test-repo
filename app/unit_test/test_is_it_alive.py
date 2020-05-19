import pytest


@pytest.mark.unittest
def test_initial(client):
    rv = client.get('/')
    assert b'Hello there!' in rv.data
