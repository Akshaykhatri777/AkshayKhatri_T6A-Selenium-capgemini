import time
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import os

o = ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)
o.add_argument('--disable-notifications')
driver.get('https://www.lenskart.com/')
driver.maximize_window()
driver.implicitly_wait(100)


driver.find_element(By.XPATH,"//a[@id='lrd1']").click()
expected = 'https://www.lenskart.com/eyeglasses.html'
actual = driver.current_url
assert expected == actual,"URL Mismatch"

driver.find_element(By.XPATH,"//select[@id='sortByDropdown']").click()
driver.find_element(By.XPATH,"//option[.='Most Viewed']").click()
folder = os.path.join(os.getcwd(),'Lenskart_practice')
os.makedirs(folder,exist_ok=True)
time_stamp = time.strftime("%Y%m%d%H%M%S")
driver.save_screenshot(f'{folder}/lenskart_{time_stamp}.png')
sleep(5)
driver.close()