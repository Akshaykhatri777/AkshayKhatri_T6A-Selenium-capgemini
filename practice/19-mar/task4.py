from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']").send_keys("C:\\Users\\Akshayyy\\Downloads\\a.java\n" "C:\\Users\\Akshayyy\\Downloads\\b.py")

