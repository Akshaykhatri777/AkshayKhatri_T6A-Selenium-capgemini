from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/webtables')
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='addNewRecordButton']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='firstName']"))).send_keys('Akshay')
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='lastName']"))).send_keys('Khatri')
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='userEmail']"))).send_keys('Akshay@123gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='age']"))).send_keys('21')
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='salary']"))).send_keys('28000')
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='department']"))).send_keys('Testing')
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submit']"))).click()
name =  wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Akshay']")))
salary = wait.until(EC.visibility_of_element_located((By.XPATH,"//td[text()='Akshay']/../td[5]")))
print(name.text,'=',salary.text)
# sleep(2)
driver.quit()



