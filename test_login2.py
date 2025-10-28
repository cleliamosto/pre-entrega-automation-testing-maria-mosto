# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():
    """
    Caso de prueba: Login exitoso en saucedemo.com
    Objetivo: validar que un usuario válido pueda acceder al inventario
    """
    # Inicia el driver de Chrome
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1️⃣ Abrir la página de login
        driver.get("https://www.saucedemo.com/")
        print("Página cargada correctamente")

        # 2️⃣ Completar usuario y contraseña
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

        # 3️⃣ Hacer clic en el botón de login
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        print("Login enviado...")

        # 4️⃣ Esperar redirección y validar URL y título
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert "/inventory.html" in driver.current_url, "No redirigió a /inventory.html"
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "El título no es 'Products'"

        print("✅ Login test passed successfully!")

        # 5️⃣ (Opcional) Pausa para ver el resultado antes de cerrar
        time.sleep(2)

    except Exception as e:
        print(f"❌ Ocurrió un error durante el test: {e}")
        raise

    finally:
        driver.quit()
        print("Navegador cerrado correctamente")


# Esto hace que el test se ejecute si corres: python test_login.py
if __name__ == "__main__":
    test_login()
