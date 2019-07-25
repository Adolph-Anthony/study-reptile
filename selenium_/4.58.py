from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()


driver.get('https://hz.58.com/zufang/?PGTID=0d100000-0004-f8f4-8162-a709355d2068&ClickID=2')

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li[1]/div[2]/h2/a')