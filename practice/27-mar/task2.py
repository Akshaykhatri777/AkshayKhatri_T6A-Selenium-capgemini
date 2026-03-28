from selenium.webdriver import Edge,EdgeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

o = EdgeOptions()
o.add_experimental_option('detach',True)
driver = Edge(options=o)
driver.implicitly_wait(20)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()

driver.find_element(By.XPATH,'//a[@href="/apparel-shoes"]').click()

def test_sort():
    sortt = driver.find_element(By.XPATH,"//select[@id='products-orderby']")
    option = Select(sortt)
    option.select_by_value('https://demowebshop.tricentis.com/apparel-shoes?orderby=11')

def test_disp():
    d = driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
    o1 = Select(d)
    o1.select_by_index(1)

def test_view():
    v = driver.find_element(By.XPATH,"//select[@id='products-viewmode']")
    o2 = Select(v)
    o2.select_by_visible_text('List')


