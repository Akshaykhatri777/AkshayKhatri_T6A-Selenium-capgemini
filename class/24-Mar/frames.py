from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
actions = ActionChains(driver)

driver.get("file:///C:/Users/Akshayyy/PyCharmMiscProject/class/24-Mar/iframe.html")
driver.find_element(By.ID,"inp1").send_keys("Input 1")

# driver.switch_to.frame(0)   #use to switch webpages frame by index
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame2']"))  #by web element Xpath
driver.find_element(By.ID,"inp2").send_keys("Input 2")
driver.switch_to.frame("n3")  #switch by name
driver.find_element(By.ID,"inp3").send_keys("Input 3")
driver.switch_to.default_content()
driver.find_element(By.ID,"inp1").send_keys("Back to 1 from 3")  #direct go back to root page or main page


# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"inp2").send_keys("Input 2/I m Back")
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"inp1").clear()
# driver.find_element(By.ID,"inp1").send_keys("Back to 1")

sleep(5)
driver.quit()