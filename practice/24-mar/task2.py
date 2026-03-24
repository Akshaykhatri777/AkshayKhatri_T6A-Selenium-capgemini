from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)
driver.get("https://www.zomato.com/india")
driver.implicitly_wait(5)
sleep(2)
login = driver.find_element(By.XPATH,"//a[text()='Log in']")
login.click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='auth-login-ui']"))
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
sleep(5)
driver.quit()