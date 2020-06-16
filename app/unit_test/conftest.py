import pytest
from python_test_project import app
from model import db as _db


def pytest_sessionstart(session):
    reset_db()


def reset_db():
    _db.init_app(app)
    with app.app_context():
        _db.drop_all()
        _db.create_all()


@pytest.fixture(scope="session")
def client():

    app.config['TESTING'] = True
    client = app.test_client()

    yield client

