from selenium.webdriver.common.by import By
from  selenium import webdriver

def test_inventory_page(logged_in_driver):
   
    try:
        driver = logged_in_driver

        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No products found on the inventory page."
    except Exception as e:
        print(f"Test failed: {e}")
        raise   
    finally:
        driver.quit()
