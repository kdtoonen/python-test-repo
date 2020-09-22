import pytest
import users
from app import app
import messages


@pytest.mark.unittest
def test_create_user_but_already_exists(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=True)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert messages.message_account_was_already_created.encode() in rv.data


@pytest.mark.unittest
def test_create_user_success(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=False)
    mocker.patch('users.create_user', return_value=True)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert messages.message_account_is_created.encode() in rv.data


@pytest.mark.unittest
def test_create_user_unsuccessful(client, mocker):
    mocker.patch('users.this_user_exists_already', return_value=False)
    mocker.patch('users.create_user', return_value=False)
    rv = client.post('/createaccount', data=dict(e_mail='test@test.com', first_name='test', last_name='test'),
                     follow_redirects=True)
    assert messages.message_error_creating_account.encode() in rv.data


@pytest.mark.unittest
def test_insert_user_and_check_password():
    with app.app_context():
        users.create_user('test@tst.com', 'test test', 'testewr')
        users.set_user_password('test@tst.com', 'thepassword')
        assert users.password_and_username_ok('test@tst.com', 'thepassword')


@pytest.mark.unittest
@pytest.mark.parametrize(
    'input_password, input_user_first_name, input_user_last_name, input_email',
    [('thepassword', 'test', 'user1', 'testuser1@bluemorpho-st.com'),
     ('thepassword', 'test', 'user2', 'testuser2@bluemorpho-st.com'),
     ('thepassword', 'test', 'user3', 'testuser3@bluemorpho-st.com'),
     ('thepassword', 'test', 'user4', 'testuser4@bluemorpho-st.com'),
     ('thepassword', 'test', 'user5', 'testuser5@bluemorpho-st.com'),
     ('thepassword', 'test', 'user6', 'testuser6@bluemorpho-st.com')])
def test_insert_users(input_password,input_user_first_name,input_user_last_name,input_email):
    with app.app_context():
        users.create_user(input_email, input_user_first_name, input_user_last_name)
        users.set_user_password(input_email, input_password)

@pytest.mark.unittest
@pytest.mark.parametrize(
    'input_password, input_password_again, expected',
    [('', '', False),
     ('Abcdef12345', 'Abcdef12346', False),
     ('abcdef1234', 'abcdef1234', False),
     ('ABCDEFGHIJK', 'ABCDEFGHIJK', False),
     ('abcdefghijk', 'abcdefghijk', False),
     ('12345678901', '12345678901', False),
     ('ABCdefGHIjk', 'ABCdefGHIjk', False),
     (' Abcdefg1234 ', ' Abcdefg1234 ', False),
     ('Abcdef12345', 'Abcdef12345', True)])
def test_password_rules(input_password, input_password_again, expected):
    assert users.password_follows_rules(input_password, input_password_again) is expected