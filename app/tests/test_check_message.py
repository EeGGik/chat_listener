import pytest
from flask import Flask
from app.urls import add_routes


@pytest.fixture
def client():
    app = Flask(__name__)
    app = add_routes(app)
    return app.test_client()


url = "/check_message"


def test_message_checker(client):
    test_body = {"user": "test user", "message": "brew"}
    response = client.post(url, json=test_body)

    assert not response.get_json()['detected']
    assert response.get_json()['bad_words'] == ""
    assert response.status_code == 200


def test_message_checker_bad_word(client):
    test_body = {"user": "test user", "message": "brew not bombs"}
    response = client.post(url, json=test_body)

    assert response.get_json()['detected']
    assert response.get_json()['bad_words'] == "bomb"
    assert response.status_code == 200


def test_message_checker_without_message(client):
    test_body = {"user": "test user"}
    response = client.post(url, json=test_body)
    assert response.get_json()["userMessage"] == 'request should contain message'
    assert response.status_code == 400


def test_message_checker_wrong_format_message(client):
    test_body = b"wrong message"
    response = client.post(url, data=test_body)
    assert "request should be JSON format! request" in response.get_json()["userMessage"]
    assert response.status_code == 400
