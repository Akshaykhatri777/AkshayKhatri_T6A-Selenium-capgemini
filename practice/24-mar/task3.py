from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.implicitly_wait(10)


driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
a1 = driver.switch_to.alert
print(a1.text)
a1.accept()
sleep(1)

driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
a2 = driver.switch_to.alert
print(a2.text)
a2.accept()
sleep(1)

driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
a3 = driver.switch_to.alert
print(a3.text)
a3.send_keys("Sending")
a3.accept()

sleep(5)
driver.quit()

