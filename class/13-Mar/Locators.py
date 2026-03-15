from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
sleep(1)
driver.find_element(By.ID, "userName").send_keys("Akshay Khatri")
driver.find_element(By.ID, "userEmail").send_keys("Aksh@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur")
driver.find_element(By.ID, "permanentAddress").send_keys("Same")

# driver.find_element(By.TAG_NAME, "input").send_keys("Akshay Khatri")
# sleep(1)
# driver.find_element(By.TAG_NAME, "input").send_keys("Aksh@gmail.com")
# #it will entered in name because first tag of input is name
# driver.find_element(By.TAG_NAME, "textarea").send_keys("Jaipur")
# sleep(1)
# driver.find_element(By.TAG_NAME, "textarea").send_keys("Same")
# sleep(2)
driver.find_element(By.ID, "submit").click()
sleep(5)
driver.quit()
