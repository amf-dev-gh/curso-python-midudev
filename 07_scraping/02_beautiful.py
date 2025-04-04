###
# Beautifull Soup 
# instalacion CMD: pip install bs4
###
# Importacion del paquete
from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
# Cambiop de user agent para evitar algunos capcha
headers = {
  'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
  print('Peticion exitosa')
  ### Parsea el html y lo deja mas manipulable en la 'sopa'
  soup = BeautifulSoup(response.text, 'html.parser')
  # .prettify() formatea la respuesta para que se vea mejor
  # print(soup.prettify())

  ### Forma sencilla de obtener el titulo de la pagina con .title
  title_tag = soup.title
  if title_tag:
    # Si existe. Con .string o.text se obtiene el contenido del tag
    print(f'El titulo de la web es: {title_tag.string}')

    # Si existe. Con .strings se obtiene el contenido de una lista por ejemplo
    # print(f'El titulo de la web es: {title_tag.string}')
  
  ### Se puede acceder a el contenedor padre del elemento (.parent) como muchas mas cosas
  # metas = soup.title.parent.find_all('meta')
  # print(metas)

  ### Buscar un precio
  # price_span = soup.find('span', class_='rc-prices-fullprice')
  # if price_span:
  #   print(f'El precio del producto es: {price_span.text}')

  ### Buscar todos los pecios
  # El nombre del tag en los argumentos no es necesario realkmente pero ayuda al momento de filtrar
  # all_prices = soup.find_all('span', class_='rc-prices-fullprice')
  # all_prices = soup.find_all(class_='rc-prices-fullprice')
  # if all_prices:
  #   for price in all_prices:
  #     print(f"Pecio es {price.text}")

  ### EJEMPLO: Buscar cada producto y obtener el nombre y precio
  products = soup.find_all(class_='rc-productselection-item')
  for p in products:
    name = p.find(class_='list-title').text
    price = p.find(class_='rc-prices-fullprice').text
    print(f'El producto "{name}" tiene un precio de {price}')

else:
  print("Fallo en la ejecucion")

