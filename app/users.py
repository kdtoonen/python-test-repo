from model import User, db
import bcrypt
import random
import string


def get_user_info(self):
    return {"Name": "Test 1"}


def create_user(user_email, first_name, last_name):
    # TODO:  fix this function
    new_user = User(first_name=first_name, last_name=last_name, email=user_email, password=generate_initial_password())
    db.session.add(new_user)
    db.session.commit()
    return True


def set_user_password(user_name, password):
    user = User.query.filter_by(email=user_name).first()
    user.password = encrypt_password(password)
    db.session.commit()


def password_and_username_ok(user_name, password):
    user_record = User.query.filter_by(email=user_name).first()
    password_in_database = user_record.password
    return bcrypt.checkpw(password.encode('utf8'), password_in_database)


def this_user_exists_already(e_mail_address):
    return True


def get_user_id():
    return 1


def generate_initial_password():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(64))


def encrypt_password(password):
    salt = bcrypt.gensalt()
    encrypted_password = bcrypt.hashpw(password.encode('utf8'), salt)
    return encrypted_password
