import pytest
from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

def test_enter_your_question():

    api_key = os.environ.get('CHATGPT_API_KEY')
    question = "How are you?"
    response = client.get(f"/chatgpt/{question}", params={"api_key": api_key})

    # Check if the response status code is 200
    assert response.status_code == 200

    # message = response.json()["message"]
    # assert len(message) < 40