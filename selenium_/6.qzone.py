from selenium import webdriver
import time
url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)

el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
time.sleep(2)
driver.switch_to.frame(el_frame)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="u"]').send_keys('1137847433')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="p"]').send_keys('xujing518333')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="login_button"]').click()

time.sleep(3)


driver.quit()