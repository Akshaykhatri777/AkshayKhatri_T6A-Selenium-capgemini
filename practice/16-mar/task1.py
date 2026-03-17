from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless') #will not open browser
driver = Chrome(options=o)
driver.get("https://amazon.in")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Mobiles")
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
sleep(2)
price = driver.find_element(By.XPATH,"//span[contains(text(),'iPhone 17 Pro Max 2')]/../../../..//span[@class='a-price']").text
print("Price of Mobile is:",price)
driver.quit()