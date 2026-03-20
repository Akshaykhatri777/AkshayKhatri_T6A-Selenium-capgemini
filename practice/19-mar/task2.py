from faulthandler import is_enabled

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Akshay")
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Khatri")
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("aks@123gmail.com")
driver.find_element(By.XPATH,"//input[@id='gender-radio-1']").click()
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys("0987654321")
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-3']").click()
driver.find_element(By.XPATH,"//input[@id='subjectsInput']").send_keys('HTML,MATHS,TESTING')
driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys(r"C:\Users\Akshayyy\Downloads\akshayPassportpic.jpg")
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Sanganer")
driver.find_element(By.XPATH,"//input[@id='react-select-3-input']").send_keys("Rajasthan")
driver.find_element(By.XPATH,"//input[@id='react-select-3-input']").send_keys(Keys.ENTER)
driver.quit()
# driver.find_element(By.XPATH,"//div[@class='css-19bb58m']").click()