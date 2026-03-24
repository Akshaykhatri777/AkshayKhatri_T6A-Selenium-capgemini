from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
o.add_argument("--disable-notifications")
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
driver = Chrome(options=o)
actions = ActionChains(driver)
driver.implicitly_wait(10)


# driver.get("https://www.python.org/downloads/")
# driver.find_element(By.XPATH,"//*[@id='touchnav-wrapper']/header/div/div[3]/div/div[3]/p[1]/a").click()

# driver.get("https://www.easemytrip.com/")

# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.find_element(By.XPATH,'//*[@id="jDate"]/span/input').click()
# nextt = driver.find_element(By.XPATH,"//*[@id='jDate']/span/div/div/div[1]/a[2]/span").click()
# driver.find_element(By.XPATH,"//*[@id='jDate']/span/div/div/div[2]/table/tbody/tr[4]/td[3]/a").click()

driver.get("https://demoqa.com/automation-practice-form")
sleep(5)
# driver.quit()