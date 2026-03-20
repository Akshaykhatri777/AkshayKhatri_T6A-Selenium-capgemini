from faulthandler import is_enabled

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
driver.maximize_window()
# driver.get("https://www.facebook.com")
# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.get("https://the-internet.herokuapp.com/checkboxesu")
driver.implicitly_wait(10)
# ele = driver.find_element(By.ID,'_R_64qjbjb9pb6amH1_')   #checking for login input field in facebook
# print(ele.is_enabled())
# print(ele.is_displayed())
# print(ele.is_selected())

# ele2 = driver.find_element(By.XPATH,'//input[@type="submit"]')
# driver.implicitly_wait(10)
# print('Enabled:',ele2.is_enabled())
# print('Displayed:',ele2.is_displayed())
# print('Selected:',ele2.is_selected())

# ele3 = driver.find_element(By.XPATH,"//button[@type='submit']")   #on naukri registration button
# print('Enabled:',ele3.is_enabled())
# print('Displayed:',ele3.is_displayed())
# print('Selected:',ele3.is_selected())


cb1 = driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]")    #on herokuapp checkbox
print('Displayed:',cb1.is_displayed())
print('Selected:',cb1.is_selected())
cb2 = driver.find_element(By.XPATH,"(//input[@type='checkbox'])[2]")
print('Displayed:',cb2.is_displayed())
print('Selected:',cb2.is_selected())


