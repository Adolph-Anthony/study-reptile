from selenium import webdriver
import time
import random

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://login.zhipin.com/?ka=header-login')

time.sleep(3)
# 账号
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[3]/span[2]/input').send_keys('')
time.sleep(2)
# 密码
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[4]/span/input').send_keys('')

# 鼠标滑块
# HK = driver.find_element_by_id('nc_2_n1z')
#
# ActionChains(driver).click_and_hold(on_element=HK).perform()
# time.sleep(0.35)
# ActionChains(driver).move_to_element_with_offset(to_element=HK, xoffset=30, yoffset=0).perform()
# time.sleep(1)
# ActionChains(driver).move_to_element_with_offset(to_element=HK, xoffset=90, yoffset=5).perform()
# time.sleep(0.5)
# ActionChains(driver).move_to_element_with_offset(to_element=HK, xoffset=160, yoffset=20).perform()
# time.sleep(0.2)
# ActionChains(driver).move_to_element_with_offset(to_element=HK, xoffset=200, yoffset=20).perform()
# time.sleep(0.3)
# ActionChains(driver).move_to_element_with_offset(to_element=HK, xoffset=250, yoffset=20).release().perform()
#
time.sleep(2)

driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div/form/div[6]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/div/div[2]/div/div[1]/input').send_keys('python')
time.sleep(1)
i = 1
while True:
    # 点击职位
    xpath = '//*[@id="container"]/div[2]/div/div[3]/div[2]/ul/li[1]'+'['+str(i)+']'
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    js = 'scrollTo(0,500)'
    driver.execute_script(js)
    time.sleep(2)
    driver.quit()
    i += 1



