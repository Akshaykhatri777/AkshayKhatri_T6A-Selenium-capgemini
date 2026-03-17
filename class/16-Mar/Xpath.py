from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument('--headless')
driver = Chrome(options=o)
driver.get('https://demoqa.com/webtables')
sleep(2)
salary = driver.find_element(By.XPATH,"//td[text()='Cantrell']/..//td[5]")
Department = driver.find_element(By.XPATH,"//td[text()='Cantrell']/..//td[6]")
print("Dept. of Cantrell is:",Department.text)
print("Salary of Cantrell is:",salary.text)
