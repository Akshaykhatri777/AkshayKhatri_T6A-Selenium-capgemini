from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in")

driver.maximize_window()
sleep(2)

driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys('shirts')
# driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("Shirts") #COMPOUND CLASS SO USE .
# driver.find_element(By.CLASS_NAME,"a-button-input").click()
# driver.find_element(By.LINK_TEXT,"Today's Deals").click() #space and case-sensitive
# driver.find_element(By.PARTIAL_LINK_TEXT,"day's D").click()
# driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(9)
driver.quit()
