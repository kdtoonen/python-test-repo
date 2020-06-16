import pytest


@pytest.mark.unittest
def test_create_user_but_already_exists(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=True)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert b'You already have an account' in rv.data


def test_create_user_success(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=False)
    mocker.patch('users.create_user', return_value=True)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert b'Your account has been created' in rv.data


def test_create_user_successful(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=False)
    mocker.patch('users.create_user', return_value=False)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert b'Something went wrong creating your' in rv.data