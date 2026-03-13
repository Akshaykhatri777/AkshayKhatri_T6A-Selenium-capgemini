# from selenium.webdriver import Chrome
# driver = Chrome()
# driver.get('https://www.amazon.com')
# sleep(5)


from time import sleep
# from selenium.webdriver import Edge
# driver = Edge()
# sleep(5)

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
sleep(5)
driver.back()   #move backward
sleep(2)
driver.forward() #to go forward
sleep(2)
driver.refresh() #to refresh page
# print(driver.current_url)
# print(driver.page_source)

#in browser travel of forward, backward and refresh


# name = driver.name
# print(name)
# sleep(2)
# driver.close() #will close that particular tab
# driver.quit() #will close all tab means browser