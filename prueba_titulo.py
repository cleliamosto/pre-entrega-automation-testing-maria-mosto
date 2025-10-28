from selenium import webdriver
import time 

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    print("titulo:", driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)
finally:
    driver.quit()


