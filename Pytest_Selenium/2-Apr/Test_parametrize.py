import pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(20)


# @pytest.fixture(autouse=True)
# def setup():
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     global driver
#     driver = Chrome(options=o)
#     driver.implicitly_wait(20)
#     driver.get('https://www.saucedemo.com/')
#     driver.maximize_window()
#     print("Open Browser")
#     yield
#     driver.quit()
#     print("\nClose Browser")

@pytest.mark.parametrize('un,passwd',[('standard_user','secret_sauce'),('akshay','aksh@123')])
def test_login(un,passwd,setup):
    setup.find_element(By.ID,"user-name").send_keys(un)
    setup.find_element(By.ID,"password").send_keys(passwd)
    setup.find_element(By.ID,"login-button").click()
    expected = "https://www.saucedemo.com/inventory.html"
    current_url = setup.current_url
    assert current_url == expected, "Login Failed"