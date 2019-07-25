from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()

# 操作浏览器对象
driver.get('https://www.baidu.com/')

# 定位元素(定位输入框且输入)
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('壁纸')
# driver.find_element_by_id('kw').send_keys('壁纸')
# driver.find_element_by_name('wd').send_keys('壁纸')
# 通过class属性进行定位
# driver.find_element_by_class_name('s_ipt').send_keys('壁纸')
# driver.find_element_by_css_selector('#kw').send_keys('壁纸')



# 点击百度一下
# driver.find_element_by_xpath('//*[@id="su"]').click()


print(driver.find_element_by_tag_name('title'))

time.sleep(2)

# 关闭浏览器
driver.close()