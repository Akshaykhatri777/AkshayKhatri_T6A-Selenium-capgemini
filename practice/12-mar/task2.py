from selenium.webdriver import Chrome,ChromeOptions #selenium package, webdriver module, chrome and chrome option class
o= ChromeOptions()
o.add_experimental_option("detach",True) #this line will not close chrome
driver = Chrome(options=o)
driver.get("https://www.amazon.com")
driver.maximize_window()  #to maximize window
# sleep()
# driver.minimize_window() #to minimize window
# driver.fullscreen_window() #no task and title bar

title = driver.title
# these are page information properties mentioned below
print(title)
