import pytest
from app import app


@pytest.fixture(scope="session")
def client():

    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        app.__init__()

    yield client


