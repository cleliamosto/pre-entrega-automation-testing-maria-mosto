# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():
    # Crear instancia del navegador
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # <-- va después de crear el driver
    wait = WebDriverWait(driver, 10)

    try:
        # 1️⃣ Abrir la página
        driver.get("https://www.saucedemo.com/")
        print("Página cargada correctamente")

        # 2️⃣ Esperar y completar el login
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        # 3️⃣ Validar que la URL y el título sean correctos
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert "/inventory.html" in driver.current_url, "No redirigió a la página de inventario"
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "El título no es 'Products'"

        print("✅ Login exitoso, test pasado correctamente")

        # Pausa opcional para ver la ventana antes de cerrar
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error durante el test: {e}")
        raise

    finally:
        driver.quit()
        print("Navegador cerrado correctamente")
