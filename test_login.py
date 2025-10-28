from selenium.webdriver.common.by import By
from selenium import webdriver
import time    
import pytest

def test_login_valiation(logged_in_driver):
    try:
        driver = logged_in_driver
        assert "inventory.html" in driver.current_url
        print("Login successful, current URL:", driver.current_url)

    except Exception as e:
        print(f"Test failed: {e}")
        raise
    finally:
        driver.quit()