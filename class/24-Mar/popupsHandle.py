from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
Simplealert = driver.find_element(By.XPATH,"//button[@id='alertBtn']")
Simplealert.click()
sleep(1)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()
promptalert = driver.find_element(By.XPATH,"//button[@id='promptBtn']")
promptalert.click()
sleep(1)
driver.switch_to.alert.send_keys("Spider Man")
sleep(2)
driver.switch_to.alert.accept()
sleep(10)
driver.quit()