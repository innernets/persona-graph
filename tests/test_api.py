import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users", json={"user_id": "test_user"})
    print(f"Create User Response: {response.status_code}, {response.json()}")
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}, response: {response.json()}"
    assert response.json() == {"message": "User test_user created successfully"}

def test_ingest_data():
    response = client.post("/api/v1/ingest/test_user", json={"content": "Python is a programming language."})
    print(f"Ingest Data Response: {response.status_code}, {response.json()}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.json()}"
    assert response.json() == {"message": "Data ingested successfully"}

def test_rag_query():
    response = client.post("/api/v1/rag/test_user/query", json={"query": "What is Python?"})
    print(f"RAG Query Response: {response.status_code}, {response.json()}")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.json()}"
    assert "answer" in response.json()

@pytest.fixture(scope="module")
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()