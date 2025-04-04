from bs4 import BeautifulSoup
# parseador de argumentos
import argparse
import requests
from urllib.parse import urljoin

# Agrega argumentos al programa que seran solicitados para iniciarlo
# para ejecutarlo, vas a la carpeta que contiene el archivo.py, abres terminal y colocas:
# python nombre-del-archivo.py
# python nombre-del-archivo.py --hepl te dice la informacion requewrida poara iniciar
parser = argparse.ArgumentParser(description='Web scraping to check SEO for a given URL')
parser.add_argument('url', type=str, help='The URL of the site you wan to scrape and check')
args = parser.parse_args()
url = args.url

headers = {
  'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
  print('\033[42mPeticion exitosa\033[0m')
  soup = BeautifulSoup(response.text, 'html.parser')
  # \033[34m a partir de este lugar todo el texto que siga tiene el color pasado (34m es azul)
  # \033[0m aqui finaliza el color previamnente pasado y comienza el color por defecto nuevamente (0m es el por defecto)
  # COLORES: https://en.wikipedia.org/wiki/ANSI_escape_code#/media/File:ANSI_sample_program_output.png
  print(f"\033[34mRevisando la pagina: {url}\033[0m")
  print(f"\033[46mSEO básico:\033[0m")
  titulo_pagina = soup.title.string
  if titulo_pagina:
    print(f'El titulo de la pagina es {titulo_pagina}')
    if len(titulo_pagina) < 70:
      print('\033[32m✅ Tiene una longitud adecuada\033[0m')
    else:
      print('\033[33m⚠️ Es demasiado largoO\033[0m')
else:
  print('Fallo en la petición')