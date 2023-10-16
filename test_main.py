import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enter_your_question():

    api_key = CHATGPT_API_KEY
    question = "How are you?"
    response = client.get(f"/chatgpt/{question}?api_key={api_key}")

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains the expected keys
    expected_keys = ["model", "messages"]
    assert all(key in response.json() for key in expected_keys)

    message = response.json()["message"]
    assert len(message) < 40