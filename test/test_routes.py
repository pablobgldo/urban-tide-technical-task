import pytest
from src.routes import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upload_csv_no_file(client):
    response = client.post('/upload-csv')
    assert response.status_code == 400
    assert response.json == {'Error': 'No file part'}


def test_upload_csv_invalid_file(client):
    data = {'file': (open('README.md', 'rb'), 'README.md')}
    response = client.post('/upload-csv', data=data)
    assert response.status_code == 400
    assert response.json == {'Error': 'Invalid file format'}


def test_upload_csv_valid_file_with_outliers(client):
    data = {'file': (open('data/test2.csv', 'rb'), 'test2.csv')}
    response = client.post('/upload-csv', data=data)
    assert response.status_code == 400
    assert response.json == {'Message': 'File not uploaded - Outliers'}


def test_upload_csv_valid_file_without_outliers(client):
    data = {'file': (open('data/test1.csv', 'rb'), 'test1.csv')}
    response = client.post('/upload-csv', data=data)
    assert response.status_code == 200
    assert response.json == {'Message': 'File successfully uploaded'}
