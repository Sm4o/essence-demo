import pytest

from essence_demo import app


@pytest.fixture
def client():
    """Client to run integration tests"""
    test_app = app.create_app()
    test_app.config["LOGIN_DISABLED"] = True
    with test_app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get("/")
    response_text = response.get_data(as_text=True)
    assert "Just a crypto dashboard" in response_text


def test_dashboard_page(client):
    response = client.get("/dashboard")
    response_text = response.get_data(as_text=True)
    assert "Crypto List" in response_text
    assert "CBSE" in response_text
