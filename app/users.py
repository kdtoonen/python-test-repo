from flask_sqlalchemy import SQLAlchemy, current_app
from datetime import datetime
db = SQLAlchemy(current_app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


def get_user_info(self):
    return {"Name": "Test 1"}


def password_and_username_ok(user_name, password):
    return True


def get_user_id():
    return 1


