from selenium import webdriver
import time
class DOuyu(object):
    def __init__(self):
        self.url= 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()


    def parse_data(self):
        '''打开网址，遍历保存'''
        time.sleep(3)
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print(room_list)
