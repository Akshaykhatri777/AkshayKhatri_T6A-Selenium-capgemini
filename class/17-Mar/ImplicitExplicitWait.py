from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.find_element(By.XPATH,"//Button[text()='Start']").click()
wait = WebDriverWait(driver, 10)
txt = wait.until(EC.visibility_of_element_located((By.XPATH, '(//h4)[2]'))).text
print(txt)
# sleep(5)
# driver.quit()