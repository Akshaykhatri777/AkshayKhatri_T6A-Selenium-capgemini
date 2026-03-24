from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)

driver.get("https://www.google.com")
sleep(5)

print(driver.current_window_handle)
print(driver.title)
driver.switch_to.new_window()
driver.get("https://www.amazon.in")
print(driver.current_window_handle)
sleep(2)
driver.switch_to.window(driver.window_handles[0])
