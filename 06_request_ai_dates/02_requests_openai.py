## Hacer una peticion a OpenAI
import requests
import json

# Para variables de entorno
# Ejecutar: pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv()  # Cargar variables del archivo .env
OPENAI_KEY = os.getenv("OPENAI_KEY")



def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  try:
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
      }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
  except requests.exceptions.RequestException as e:
   print("Error e la solicitud", e)

  
api_response = call_openai_gpt(OPENAI_KEY, "Escribe una historia breve sobre la programacion")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])