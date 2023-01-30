import pytest

from sensor_app import app


@pytest.fixture
def client():
    app.config.update({'TESTING': True})

    with app.test_client() as client:
        yield client

def test_helloworld(client):
    resp = client.get('/hello')
    assert b'Hello World' in resp.data