from playwright.sync_api import sync_playwright
import argparse
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description='Scraping para obtener seguidores deuna cuenta de ig')
parser.add_argument('url', type=str, help='Web de noticias a escrapear')
args = parser.parse_args()
url = args.url

# Solo sirve paora obtener los titulos de las noticias del periodico levante-emv (A MEJORAR)
# python scrap_news.py https://www.levante-emv.com

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.wait_for_load_state()

    # Aceptar cookies si el botón está presente
    btn_cookies = page.locator('#didomi-notice-agree-button')
    if btn_cookies.is_visible():
        btn_cookies.click()
        page.wait_for_load_state()

    # Obtener todos los h1
    titles = page.locator('.ft-org-cardHome__mainTitle').all()

    print("**Noticias encontradas**")
    for title in titles:
        link = title.locator('a').get_attribute('href')
        print(f'\033[33m⚜️ {title.inner_text()}\033[0m\n Link noticia --> {urljoin(url,link)}\033')

    browser.close()