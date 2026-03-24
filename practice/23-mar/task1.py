#task 1
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(10)

hovEl = driver.find_element(By.XPATH,'//button[@class="dropbtn"]')
actions = ActionChains(driver)
actions.scroll_by_amount(0,1000).perform()
actions.pause(2).move_to_element(hovEl).perform()

dbl = driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
actions.pause(1).double_click(dbl).perform()
actions.pause(1).scroll_by_amount(0,400).perform()


drag = driver.find_element(By.XPATH,'//div[@ID="draggable"]')
drop = driver.find_element(By.XPATH,'//div[@ID="droppable"]')
actions.pause(2).drag_and_drop(drag,drop).perform()
sleep(4)
driver.quit()