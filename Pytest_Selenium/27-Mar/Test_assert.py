import pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)
driver.get('https://demowebshop.tricentis.com')
driver.maximize_window()
driver.implicitly_wait(100)

# def test_equality():
#     l = ['apple', 'banana', 'orange']
#     assert 5==5, "Equal"
#     assert 'apple' in l
#     # assert 5==10," Not Equal "

@pytest.mark.regression
def test_click():
    driver.find_element(By.XPATH,"//a[text()='Register']").click()

def test_data():
    driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
    driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys('Akshay')
    driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('Khatri')
    driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('aksh@123gmail.com')

def test_passwd():
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('Abc@123')
    driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('abc@123')