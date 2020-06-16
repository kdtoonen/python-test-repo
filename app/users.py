from model import Users, db


def get_user_info(self):
    return {"Name": "Test 1"}


def create_user(user_email, first_name, last_name):
    new_user = Users(first_name, last_name, user_email)
    db.session.add(new_user)
    db.session.commit()


def password_and_username_ok(user_name, password):
    return True


def this_user_exists_already(e_mail_address):
    return True


def get_user_id():
    return 1


def generate_initial_password():
    pass
