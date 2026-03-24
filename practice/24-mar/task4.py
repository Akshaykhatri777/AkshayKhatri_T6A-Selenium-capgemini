#task_4
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions


o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
google = driver.current_window_handle
print(google)
print(driver.title)
print(driver.current_url)

driver.switch_to.new_window()
driver.get("https://www.amazon.com")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

driver.switch_to.new_window()
driver.get("https://flipkart.com/")
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

allTabs = driver.window_handles
for i in allTabs:
    driver.switch_to.window(i)
    if i != google:
        driver.close()

sleep(10)
driver.quit()