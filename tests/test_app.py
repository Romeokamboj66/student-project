import pytest
from app import app, init_db

@pytest.fixture
def client():
    init_db()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_and_login(client):
    response = client.post('/register', data={'username': 'test', 'email': 'test@test.com', 'password': '1234'}, follow_redirects=True)
    assert b"Registration successful" in response.data

    response = client.post('/login', data={'username': 'test', 'password': '1234'}, follow_redirects=True)
    assert b"Welcome test" in response.data

