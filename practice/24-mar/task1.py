from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)
driver.get('https://x.com/?lang=en-in')
driver.maximize_window()
sleep(2)
sign = driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(sign)
driver.find_element(By.XPATH,"//span[.='Sign up with Google']").click()
sleep(2)
driver.quit()