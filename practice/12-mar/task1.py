from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.wikipedia.com")
driver.maximize_window()
driver.refresh()
title = driver.title
print(title)
driver.get("https://www.amazon.com")
sleep(3)
driver.back()
sleep(3)
driver.close()
