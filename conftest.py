# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def _make_driver():
    """Crea una instancia de Chrome configurada."""
    opts = Options()
    # Si querés ejecutar sin ventana, podés activar el modo headless así:
    # opts.add_argument("--headless=new")
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=opts)

@pytest.fixture
def driver():
    """Fixture base: abre y cierra el navegador."""
    drv = _make_driver()
    drv.implicitly_wait(5)
    yield drv
    drv.quit()

@pytest.fixture
def logged_in_driver(driver):
    """Fixture extendido: hace login en saucedemo y deja el inventario listo."""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    yield driver
