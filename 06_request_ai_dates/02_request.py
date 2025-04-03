# Como hacer peticiones a APIS con Phython

### SIN Dependencias
# Forma mas 'Dificil' o verbosa
# Importar
import urllib.error
import urllib.request
import json

api_posts = 'https://jsonplaceholder.typicode.com/posts/'

try:
  # urllib abre y consulta la url que le paso
  response = urllib.request.urlopen(api_posts)
  # leo la respuesta y la asigno a data
  data = response.read()
  # cargo la respuesta decodificada con json.loads y la almaceno en una variable
  json_data = json.loads(data.decode('utf-8'))
  print(json_data)
  # cierro la respuesta
  response.close()
except urllib.error.URLError as e:
  print(f"Error en la solicitud {e.reason}")

### CON dependencia (requests)
# para intalar esta dependencia en CMD: pip install requests
import requests

print("\nMetodo GET:")
api_posts = 'https://jsonplaceholder.typicode.com/posts/'
response = requests.get(api_posts)
json = response.json()
print(json[0])

print("\nMetodo POST:") # El metodo PUT es igual
api_posts = 'https://jsonplaceholder.typicode.com/posts/'
try:
  input = {
    "title":"midu",
    "body":"dev",
    "userId": 5
  }
  response = requests.post(api_posts, json=input)
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print("Error e la solicitud", e)
