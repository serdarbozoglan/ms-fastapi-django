from app.main import app # from app module main module and app varibale --> FastAPI instance
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_home():
    response = client.get('/')  # similar to --> r = requests.get. Stop the server and run the test
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']

def test_post_home():
    response = client.post('/')  # similar to --> r = requests.post. Stop the server and run the test
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {'hello':'world'}
