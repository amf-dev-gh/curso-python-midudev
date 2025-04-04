from bs4 import BeautifulSoup
import requests
# PAquete para trabajar con url (En este caso unir la url inicial con los links de la web)
from urllib.parse import urljoin

def scrap_url(url):
  headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    print('Peticion exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')

    ### Extraer ltodos los titulos H1
    titulos = [titulo.string for titulo in soup.find_all('h1')]
    print(titulos)

    ### Extraer todos los enlaces
    enlaces = [urljoin(url, enlace.get("href")) for enlace in soup.find_all('a')]
    # print(enlaces)

    ### Extraer todo el texto de la web
    # all_text = soup.get_text()
    # print(all_text)

    ### Extraer texto del main
    # main_text = soup.find('main').get_text()
    # print(main_text)

    ### Extraer el texto del contenedor con id: mw-content-text (DOS MANERAS)
    # content_text = soup.find(id='mw-content-text').get_text()
    content_text = soup.find('div', {'id':'mw-content-text'}).get_text()
    print(content_text)
  else:
    print("Error en la petición")

# ----------- Llamado al metodo ---------------------

scrap_url('https://es.wikipedia.org/wiki/Web_scraping')