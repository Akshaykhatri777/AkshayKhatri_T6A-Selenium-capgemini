from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//span[text()="✕"]').click()

Myntra = driver.find_element(By.XPATH,'//a[@href="https://www.myntra.com/"]')
actions = ActionChains(driver)
origin = ScrollOrigin.from_element(Myntra)
actions.pause(2).scroll_from_origin(origin,0,100).perform()
Myntra.click()

driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//a[@href="https://www.cleartrip.com/"]').click()
driver.switch_to.window(driver.window_handles[2])
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//a[@href="https://www.shopsy.in"]').click()
driver.switch_to.window(driver.window_handles[3])
print(driver.current_window_handle)
print(driver.title)
print(driver.current_url)

sleep(10)
driver.quit()