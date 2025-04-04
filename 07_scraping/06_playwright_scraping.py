# Utilizandolo de forma programatica
#pytest ./04_playwright.py

# Importar API sincrona
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

url='https://midu.dev'

with sync_playwright() as p:
  # Aca se eligue el navegadopr a utilizar y sus caracteristicas... headlees o no, utilizar tu navegadors.. timeout.. proxi

  # Ejecuta el navegador
  browser = p.chromium.launch()
  # browser = p.chromium.launch(headless=False, slow_mo=2000) # Para que abra el navegador mienstras scrapea y que vaya mas lento para ver los pasos
  # Abre nueva pagina
  page = browser.new_page()
  # Va a una url
  page.goto(url)
  # Buscar el primer 'articulo' de la pagina y el primer enlace
  firt_article_anchor = page.locator('article a').first
  # HAce click en el objeto encontrado
  firt_article_anchor.click()
  # Esperar el estado de la pagina
  page.wait_for_load_state()
  ## Encontrar la primera imagen
  # first_imagew = page.locator('main img').first
  # img_src = first_imagew.get_attribute('src')
  # print("La imagen del primer curso es: ", img_src)

  ## REcuperar un elemento con xPath (se extrrae del html click derecho en el elemento)
  # first_imagew = page.locator('xpath=/html/body/div[1]/main/div[1]/img')
  # img_src = first_imagew.get_attribute('src')
  # print("La imagen del primer curso es: ", img_src)

  ## Recuperar un elemento a partir de texto
  curso_content_container = page.locator("text='Contenido del curso'")
  print(curso_content_container)


  browser.close()