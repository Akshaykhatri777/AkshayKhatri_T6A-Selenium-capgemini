import os
import time
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com/")
# print(driver.title)
# expected = "Google"
# actual = driver.title
# # assert "Google" in driver.title
# assert expected == actual, "Title does not match"
# driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("Akshay")

# driver.save_screenshot("screenshot1.png")
folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)
# driver.save_screenshot(f'{folder}/screenshot.png')

ele = driver.find_element(By.XPATH,"//textarea[@title='Search']")
ele.send_keys("Akshay")
ele.screenshot(f'{folder}/ele_screenshot.png')    #element screenshot  #same name will override previous image
timestamp = time.strftime("%Y-%m-%d-%H:%M:%S")
ele.screenshot(f'{folder}/ele_screenshot_{timestamp}.png')



# driver.get("https://www.amazon.in/")
# bestSeller = driver.find_element(By.XPATH,"//a[text()='Bestsellers']")
# bestSeller.click()
# expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
# actual = driver.title
# assert expected == actual
# print("Success")
sleep(5)
# driver.quit()