import pytest
import theproject


@pytest.mark.unittest
def test_initial(client):
    rv = client.get('/')
    assert b'Hello World!' in rv.data




