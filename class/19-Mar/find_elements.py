from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
driver.maximize_window()
# driver.get("https://www.google.com")
# driver.implicitly_wait(10)
# links = (driver.find_elements(By.TAG_NAME,'a'))
# print(len(links))
# for i in links:
#     print(i.text)       #printing the text of all element



# driver.get("https://www.amazon.in")
# driver.implicitly_wait(10)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("abc")
# driver.find_element(By.ID,"nav-search-submit-button").click()
# links = (driver.find_elements(By.XPATH,"//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']"))
# print(len(links))
# links[4].click()


# driver.get("https://www.google.com")
# driver.implicitly_wait(10)
# ele = driver.find_element(By.XPATH,"//a[@class='gb_A']")
# print(ele.get_attribute("aria-label"))


driver.get("https://www.amazon.in")
driver.implicitly_wait(10)
lst = driver.find_elements(By.XPATH,"//li[@class='nav-li']//a")
for i in lst:
    print(i.text,"=",i.get_attribute("href"))
