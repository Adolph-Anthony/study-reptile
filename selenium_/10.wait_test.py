from selenium import webdriver

driver = webdriver.Chrome()

# 设置位置之后的所有元素定位操作都有最大等待时间十秒,在十秒内会定期进行元素定位，超过时间设置后将会报错

driver.get('http://www.baidu.com')

el = driver.find_element_by_xpath('//*[@id="lg"]/img[1]')
print(el)