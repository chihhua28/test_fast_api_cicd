from typing import Union
from fastapi import FastAPI
import requests
import os
import json

app = FastAPI()

@app.get("/chatgpt/{prompt}")

def enter_your_question(api_key, question: Union[str, None] = None):
    api_key = os.environ.get('CHATGPT_API_KEY')
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

@app.get("/cocktails/{cocktail_name}")
def get_cocktail_by_name(cocktail_name: str):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}"
    response = requests.get(url)
    data = response.json()
    cocktails_data = []
    for drink in data['drinks']:    
        cocktail_info = {
            'Drink': drink['strDrink'],
            'Instructions': drink['strInstructions']
        }
        cocktails_data.append(cocktail_info)

    with open('cocktails.json', 'w') as json_file:
        json.dump(cocktails_data, json_file, indent=4)

    with open('cocktails.json', 'r') as json_file:
        cocktails_json = json.load(json_file)

    return(cocktails_json)