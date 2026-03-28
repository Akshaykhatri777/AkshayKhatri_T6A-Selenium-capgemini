from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(20)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()

def test_fb():
    fb = driver.find_element(By.XPATH, "//a[.='Facebook']")
    action = ActionChains(driver)
    action.scroll_to_element(fb).pause(3).click(fb).perform()

def test_login():
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, "(//input[@name='email'])[2]").send_keys("aksh123@gmail.com")
    driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("aksh@123")
    driver.find_element(By.XPATH, "(//span[.='Log in'])[5]").click()