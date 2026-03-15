from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students",
        json={"id": 1, "name": "Alice"}
    )

    assert response.status_code == 200
    assert response.json()["student"]["name"] == "Alice"


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "id": 1,
            "title": "Отчет по практике",
            "student_id": 1
        }
    )

    assert response.status_code == 200
    assert response.json()["task"]["title"] == "Отчет по практике"
