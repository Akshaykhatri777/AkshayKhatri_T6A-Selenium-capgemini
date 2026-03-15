from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")

sleep(2)
driver.find_element(By.LINK_TEXT,"Downloads").click()
sleep(2)
driver.find_element(By.LINK_TEXT,"other languages exist").click()
sleep(2)
title = driver.title
sleep(2)
print(title)
