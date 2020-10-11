import pytest
from flask import Flask
from app.urls import add_routes


@pytest.fixture
def client():
    app = Flask(__name__)
    app = add_routes(app)
    return app.test_client()


def test_health_check(client):
    response = client.get("/manage/health")
    assert response.json == {"status": "ok"}
    assert response.status_code == 200
