## IGUAL A OPENAI
# No tengo cuenta de deepseek no, voy a usar por ahora

import json
import requests

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

DEEPSEEK_API_KEY = "xxxxxxxxxxxxxxx"
api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])