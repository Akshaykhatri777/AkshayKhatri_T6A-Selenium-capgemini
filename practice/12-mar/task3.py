from selenium.webdriver import Chrome,ChromeOptions
o= ChromeOptions()
o.add_experimental_option("detach",True) #this line will not close chrome
driver = Chrome(options=o)
driver.get("https://www.amazon.com")
driver.maximize_window()
print(driver.current_url)