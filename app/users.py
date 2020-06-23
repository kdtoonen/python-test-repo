from model import User
from model import db
import bcrypt
import random
import string
import uuid
import re
import mailer
import sys


def get_user_info(self):
    return {"Name": "Test 1"}


def create_user(user_email, first_name, last_name):
    # TODO:  fix this function
    reset_code = str(uuid.uuid4())
    new_user = User(first_name=first_name, last_name=last_name, email=user_email, password=generate_initial_password(),
                    reset_code=reset_code)
    db.session.add(new_user)
    db.session.commit()
    return confirmation_email_sent(user_email, reset_code)


def set_user_password(user_name, password):
    user = User.query.filter_by(email=user_name).first()
    user.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    db.session.commit()


def reset_user_password(user_name, password, reset_code):
    user = User.query.filter_by(email=user_name, reset_code=reset_code).first()
    user.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    user.reset_code = str(uuid.uuid4())
    db.session.commit()


def password_and_username_ok(user_name, password):
    user_record = User.query.filter_by(email=user_name).first()
    password_in_database = user_record.password
    return bcrypt.checkpw(password.encode('utf8'), password_in_database)


def this_user_exists_already(e_mail_address):
    if User.query.filter_by(email=e_mail_address).count() >= 1:
        return True
    else:
        return False


def get_user_id():
    return 1


def generate_initial_password():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(64))


def check_new_user_first_last_and_user_name(user_name, user_first_name, user_last_name):
    status = []
    if user_name == '' or None:
        status.append('E-Mail cannot be empty')
    if user_first_name == '' or None:
        status.append('first name cannot be empty')
    if user_last_name == '' or None:
        status.append('last name cannot be empty')
    return status


def password_follows_rules(password, password_again):
    return_value = False
    if password != password_again:
        return_value = False
    elif len(password) < 11:
        return_value = False
    elif not re.search("[a-z]", password):
        return_value = False
    elif not re.search("[A-Z]", password):
        return_value = False
    elif not re.search("[0-9]", password):
        return_value = False
    elif re.search("\s", password):
        return_value = False
    else:
        return_value = True
    return return_value


def confirmation_email_sent(email_address, reset_code):
    message_body = 'Subject: Confirm your e-mail and create login  \n\n' \
                   'Welcome to Reservatron. Please confirm that you have ' \
                   'created an account with us by following the link below. \n\n' \
                   '<a href="http://localhost:5000/resetpassword?reset_code=' + reset_code + '&email=' \
                   + email_address + '">. ' \
                                      'CONFIRM ACCOUNT </a> \n\n' \
                                      'If the link does not work, please copy paste the following url in your browser: \n' \
                                     'http://localhost:5000/resetpassword?reset_code=' + reset_code + '&email=' + email_address + '\n\n' \
                                    'Thanks for using Reservatron.\n\n' \
                                    'Reservatron '
    return send_message_trough_mailer_and_return_boolean_status(email_address, message_body)


def send_message_trough_mailer_and_return_boolean_status(email_address, message_body):
    try:
        mailer.send_message(email_address, message_body)
        return_boolean = True
    except Exception as e:
        print(e, sys.stderr)
        return_boolean = False
    return return_boolean
