import pytest


@pytest.mark.unittest
def test_initial(client):
    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert b'logged on' in rv.data