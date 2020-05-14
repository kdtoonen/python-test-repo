import pytest


@pytest.mark.unittest
def test_initial(client):
    rv = client.get('/')
    assert b'Users Table' in rv.data
