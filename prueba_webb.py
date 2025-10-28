# prueba_web.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 1) Ir al login y loguear
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # 2) Validar que estamos en inventario
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert "/inventory.html" in driver.current_url, "No redirigió a /inventory.html"
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "El título del inventario no es 'Products'"

    # 3) Agregar el primer producto del listado
    add_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[id^='add-to-cart']"))
    )
    add_buttons[0].click()

    # 4) Esperar el badge del carrito y validar que sea '1'
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    badge_text = badge.text   # <-- esto ya es str
    print("Badge:", badge_text)
    assert badge_text == "1", f"Se esperaba badge '1', llegó '{badge_text}'"

    # 5) Ir al carrito y verificar que haya un ítem
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    assert len(cart_items) >= 1, "No se encontró el producto en el carrito"

    # (Opcional) mostrar el nombre del producto
    name = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    print("Producto en carrito:", name)

finally:
    driver.quit()
