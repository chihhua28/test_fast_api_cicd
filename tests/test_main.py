import pytest
from fastapi.testclient import TestClient
from app.main import app
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

def test_get_cocktail_by_name():

    response = client.get("/cocktails/long island")
    data = response.json()


    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains the expected keys
    expected_keys = ["Drink", "Instructions"]

    for item in data:
        assert all(key in item for key in expected_keys), f"Response does not contain the expected keys for cocktail: {item['strDrink']}"