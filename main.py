from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/chatgpt/{prompt}")

def enter_your_question(api_key, question: Union[str, None] = None):
    prompt = question

    response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    },
    json = {
        'model': 'gpt-3.5-turbo', 
        'messages' : [{"role": "user", "content": prompt}]
    })

    json = response.json()
    return(json)