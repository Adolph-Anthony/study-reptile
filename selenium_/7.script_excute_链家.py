from selenium import webdriver
import time
url = 'https://hz.lianjia.com/'

driver = webdriver.Chrome()

driver.get(url)
time.sleep(2)
# js = 'scrollTo(x,y)'   x 水平距离  y  上下距离

js = 'scrollTo(0,500)'

driver.execute_script(js)

driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]/a/img').click()
time.sleep(2)
driver.quit()