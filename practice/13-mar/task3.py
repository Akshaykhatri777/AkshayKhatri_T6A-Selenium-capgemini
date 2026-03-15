from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
sleep(2)
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("abc123")
sleep(5)
driver.quit()