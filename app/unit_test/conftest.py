import pytest
from python_test_project import app
from model import db


@pytest.fixture(scope="session")
def reset_db():
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()


@pytest.fixture(scope="session")
def client():

    app.config['TESTING'] = True
    client = app.test_client()

    yield client

