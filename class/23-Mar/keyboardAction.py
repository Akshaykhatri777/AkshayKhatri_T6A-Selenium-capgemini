from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)

# driver.get("https://www.amazon.in")
# driver.get("https://demoqa.com/text-box")
# driver.get('https://demoqa.com/buttons')
# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
driver.get("https://demoqa.com/droppable")

driver.maximize_window()
driver.implicitly_wait(10)

#FOR ENTER
# ele = (driver.find_element(By.ID,'twotabsearchtextbox'))
# ele.send_keys("Shoes")
# # driver.find_element(By.ID,'nav-search-submit-button').click()
# ele.send_keys(Keys.ENTER)


#FOR COPY-PASTE
# ele = driver.find_element(By.ID,"currentAddress")
# ele.send_keys("Sanganer, Jaipur")
# ele.send_keys(Keys.CONTROL+"a")
# ele.send_keys(Keys.CONTROL+"c")
#
# ele2 = driver.find_element(By.ID,"permanentAddress")
# ele2.send_keys(Keys.CONTROL+"v')

#3 Types of click
# actions = ActionChains(driver)
# normal_click = driver.find_element(By.XPATH,"//button[text()='Click Me']")
# actions.click(normal_click).perform()
# double_click = driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
# actions.double_click(double_click).perform()
# right_click = driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
# actions.context_click(right_click).perform()

#SCROLL
# sleep(5)
# ele4 = driver.find_element(By.XPATH,"(//span[@class='a-truncate-cut'])[20]")
# # actions.scroll_to_element(ele4).pause(5).perform()
# # sleep(2)
# # actions.click(ele4).pause(5).perform()
# # sleep(3)
# # actions.scroll_by_amount(0,1000).perform()
# # sleep(2)
# # actions.scroll_by_amount(0,200).perform()
# origin = ScrollOrigin.from_element(ele4)
# actions.scroll_from_origin(origin,0,100).perform()

# #MOVE TO
# sleep(3)
# ele5 = driver.find_element(By.XPATH,"//a[@class='nav-a nav-a-2   nav-progressive-attribute']")
# actions.move_to_element(ele5).perform()

#CLICK AND HOLD
# ele6 = driver.find_element(By.XPATH,"//input[@id='password']")
# ele6.send_keys("Akshay")
# sleep(2)
# ele7 = driver.find_element(By.XPATH,"//button[@tabindex='0']")
# sleep(2)
# actions.click_and_hold(ele7).pause(3).release().perform()

#DRAG AND DROP
# drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
# drop = driver.find_element(By.XPATH,"//div[@id='droppable']")
# sleep(2)
# actions.drag_and_drop(drag,drop).perform()

sleep(5)
# driver.quit()