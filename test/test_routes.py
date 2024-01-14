import pytest
from src.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload_csv_route(client):
    response = client.post('/upload-csv')
    assert response.status_code == 400
