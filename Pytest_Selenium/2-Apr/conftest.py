import pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    global driver
    driver = Chrome(options=o)
    driver.implicitly_wait(20)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    print("Open Browser")
    yield
    driver.quit()
    print("\nClose Browser")