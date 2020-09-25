import pytest


@pytest.mark.unittest
def test_login_success(client, mocker):
    mocker.patch('users.password_and_username_ok', return_value=True)
    mocker.patch('users.get_user_id', return_value=1)
    mocker.patch('users.get_user_info', return_value={"first_name": "test", "last_name": "test"})

    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert b'logged on' in rv.data


@pytest.mark.unittest
def test_login_fail(client, mocker):
    mocker.patch('users.password_and_username_ok', return_value=False)

    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    assert b'login failed' in rv.data


@pytest.mark.unittest
def test_log_off(client, mocker):
    mocker.patch('users.password_and_username_ok', return_value=True)
    mocker.patch('users.get_user_id', return_value=1)
    mocker.patch('users.get_user_info', return_value={"first_name": "test", "last_name": "test"})
    rv = client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)
    rv = client.get('/logoff')
    assert b'Logged off' in rv.data
