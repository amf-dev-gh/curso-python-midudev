###
# https://playwright.dev/python/docs/intro

# Instalacion de la dependencia: en CMD: 
# pip install pytest-playwright

# Instalacion de los navegadores headless que utiliza
# playwright install

# Comando pytest para realizar pruebas
# pytest ./nombre_del_archivo.py
###

## Test de EJEMPLO de la web
import re # Regular expression
from playwright.sync_api import Page, expect # Importacion de la dependencia

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()