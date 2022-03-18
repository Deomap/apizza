import pytest

from app import app
from fastapi.testclient import TestClient
from api.dependencies.auth import verify_token

client = TestClient(app)


# DEPENDENCIES
scopes = ['authed']


class User:
    id = 1


@pytest.fixture
def client_non_authed():
    """
    Return an API Client
    """
    app.dependency_overrides = {}
    return TestClient(app)


@pytest.fixture
def client_authed():
    """
    Returns an API client which skips the authentication
    """
    def skip_auth():
        return {
            "user": User,
            "scopes": scopes,
        }
    app.dependency_overrides[verify_token] = skip_auth
    return TestClient(app)

# TESTS ===================================================


def test_authed_user(client_authed):
    """
    Verify that logged-in users can not access the user functions excluding create
    """
    # Create order
    response = client_authed.post(
        "/orders/1",
        json={
            "type": "string",
            "delivery_adds": "string",
            "status": "string",
            "products": [{
                "name": "string",
                "price": 0,
                "order_id": 0
            }],
            "price": 0
        },)
    assert response.status_code == 200, response.text

    # Get all orders
    response = client_authed.get(
        "/orders/",
    )
    assert response.status_code == 200, response.text


def test_non_authed_user(client_non_authed):
    """
    Verify that not logged-in users can not access the user functions excluding create
    """
    # Create order
    response = client_non_authed.post(
        "/orders/1",
        json={
            "type": "string",
            "delivery_adds": "string",
            "status": "string",
            "products": [{
                "name": "string",
                "price": 0,
                "order_id": 0
            }],
            "price": 0
        }, )
    assert response.status_code == 401, response.text



