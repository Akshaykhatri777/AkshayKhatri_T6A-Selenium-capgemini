from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument('--headless') #will not open browser
driver = Chrome(options=o)
# driver.get('https://the-internet.herokuapp.com/tables')
# sleep(1)
# # due = driver.find_element(By.XPATH,"//td[text()='Bach']/..//td[4]")
# due = driver.find_element(By.XPATH,"//td[text()='Tim']//following-sibling::td[2]")
#
# # Department = driver.find_element(By.XPATH,"//td[text()='Cantrell']/..//td[6]")
# # print("Dept. of Cantrell is:",Department.text)
# print(" Due of Tim is:",due.text)