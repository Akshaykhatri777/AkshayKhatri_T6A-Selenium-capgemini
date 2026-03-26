import os
import time
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)

driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
# if driver.current_url != "https://www.saucedemo.com/inventory.html":
#     ele = driver.find_element(By.XPATH,"//div[@class='login_wrapper-inner']")
#     ele.screenshot(f'{folder}/login_screenshot.png')
expected = "https://www.saucedemo.com/inventory.html"
actual = driver.current_url
assert expected == actual, "Login failed"
sleep(2)
driver.quit()