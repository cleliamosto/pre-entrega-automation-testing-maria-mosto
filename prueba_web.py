from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    #login page
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type= 'submit']").click()
    time.sleep(2)

    # validacion de la redireccion de la página
    assert '/inventory.html' in driver.current_url  

    # interacciones
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito.text == "1"

    print("Test passed successfully")

    time.sleep(2)
    
    
finally:
    driver.quit()


