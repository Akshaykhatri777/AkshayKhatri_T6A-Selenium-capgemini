from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


o= ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument('--headless')
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.decathlon.in/?irclickid=X5M04Z231xyZWZszSawWnWpOUkuz:Xy-EzNkT80&sharedid=https://www.zingoy.com/&irpid=5987434&user_id=&irgwc=1&afsrc=1&gad_source=1")
driver.find_element(By.XPATH,"//div[@class='flex flex-col items-center justify-start gap-1']").click()

