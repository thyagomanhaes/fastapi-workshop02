import pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200    


def test_read_main_json():
    response = client.get("/")    
    assert response.json() == {"message": "Hello World"}


def test_size_products_list():
    response = client.get("/")    
    assert len(response.json()) == 1
