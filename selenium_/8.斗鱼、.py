from selenium import webdriver
import time
class Douyu(object):
    def __init__(self):
        self.url= 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()


    def parse_data(self):
        '''打开网址，遍历保存'''
        # self.driver.implicitly_wait(10)  # 隐式等待，最长等20秒
        self.driver.get(self.url)
        # xpath查找资源
        time.sleep(4)

        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        # print(room_list)
        print(len(room_list))
        # time.sleep(10)
        data_list = []
        for room in room_list:
            temp = {}
            temp['title'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/h3').text
            temp['type'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/span').text
            temp['owner'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/h2').text
            temp['num'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/span').text
            data_list.append(temp)
        return data_list
    def save(self, data_list):
        for data in data_list:
            print(data)


                    # print(temp)
    def run(self):
        self.driver.get(self.url)
        while True:
            # 打开url得到列表
            data_list = self.parse_data()
            self.save(data_list)

            try:
                # 找到下一页按钮
                el_next = self.driver.find_element_by_xpath('//*[contains(text(), "下一页")]')
                # 滚动
                self.driver.execute_script('scrollTo(0,100000)')
                # print(el_next)
                el_next.click()
            except:
                break
if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()