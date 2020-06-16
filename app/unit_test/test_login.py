import pytest


@pytest.mark.unittest
def test_login_success(client, mocker):
    mocker.patch('users.password_and_username_ok', return_value=True)
    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert b'logged on' in rv.data


@pytest.mark.unittest
def test_login_fail(client, mocker):
    mocker.patch('users.password_and_username_ok', return_value=False)
    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert b'login failed' in rv.data