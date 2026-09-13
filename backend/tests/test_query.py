# Test that the API is working and can answer questions correctly.

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_query():
    response = client.post(
        "/query",
        json={
            "question": "What is overfitting?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["answer"], str)
    assert isinstance(data["sources"], list)
    
def test_query_invalid_input():
    response = client.post(
        "/query",
        json={}
    )

    assert response.status_code == 422