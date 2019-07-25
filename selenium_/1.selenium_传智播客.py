from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.itcast.cn/')

ret = driver.find_elements_by_tag_name('h2')
print(ret[0].text) #

ret = driver.find_elements_by_link_text('黑马程序员')
print(ret[0].get_attribute('href'))

driver.quit()