from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(200), nullable=False)
    LastName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


def get_user_info(self):
    return {"Name": "Test 1"}


def password_and_username_ok(user_name, password):
    return True


def this_user_exists_already(e_mail_address):
    return True


def get_user_id():
    return 1


