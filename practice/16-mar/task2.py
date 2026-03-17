from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless') #will not open browser
driver = Chrome(options=o)
driver.get("https://flipkart.in")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH,"//input[@class='nw1UBF v1zwn25']").send_keys("Shoes")
driver.find_element(By.XPATH,"//button[@class='XFwMiH']").click()
sleep(2)
price = driver.find_element(By.XPATH,"((//div[@class='Fo1I0b'])[3]/..//div)[3]")
print(price.text)
sleep(5)
driver.quit()