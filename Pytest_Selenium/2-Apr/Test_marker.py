import pytest
from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = EdgeOptions()
o.add_experimental_option("detach", True)
driver = Edge(options=o)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(20)
driver.get('https://demowebshop.tricentis.com')
driver.maximize_window()

@pytest.mark.smoke
def test_click():
    driver.find_element(By.XPATH,"//a[text()='Register']").click()

@pytest.mark.smoke
def test_data():
    driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
    driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys('Akshay')
    driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('Khatri')
    driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('aksh@123gmail.com')

@pytest.mark.regression
def test_passwd():
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('Abc@123')
    driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('abc@123')

# driver.close()
#driver.quit()