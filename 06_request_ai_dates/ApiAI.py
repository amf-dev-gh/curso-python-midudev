import requests
from dotenv import load_dotenv
import os

class ApiAI:
  def __init__(self, api_url, api_key, model):
    self.apiUrl = api_url
    self.api_key = api_key
    self.model = model

  def call (self, prompt):
    try:
      headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
      }
      data = {
          "model": self.model,
          "messages": [{"role": "user", "content": prompt}]
        }
      response = requests.post(self.apiUrl, json=data, headers=headers)
      data_json = response.json()
      print(data_json["choices"][0]["message"]["content"])

    except requests.exceptions.RequestException as e:
      print("Error e la solicitud", e)
    
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

openia_api = ApiAI("https://api.openai.com/v1/chat/completions",OPENAI_KEY, "gpt-4o-mini")
openia_api.call("Python usa clases como Java?")