from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users_initially_empty():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_user_valid():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "disabled": False
    }

    response = client.post("/users", json=user_data)
    assert response.status_code in (200, 201)
    assert response.json()["username"] == "testuser"


def test_get_users_after_create():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_create_user_invalid_payload():
    invalid_user = {
        "username": "sin_email"
    }

    response = client.post("/users", json=invalid_user)
    assert response.status_code == 422
