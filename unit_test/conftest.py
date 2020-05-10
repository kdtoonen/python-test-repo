import pytest
import theproject


@pytest.fixture(scope="session")
def client():

    theproject.app.config['TESTING'] = True
    client = theproject.app.test_client()
    with theproject.app.app_context():
        theproject.init_db()

    yield client


