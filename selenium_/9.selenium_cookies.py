from selenium import webdriver
url = 'http://www.baidu.com/'
options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument("--headless") # 开启无界面模式
options.add_argument("--disable-gpu") # 禁用gpu

# options.set_headles() # 无界面模式的另外一种开启方式
driver = webdriver.Chrome(chrome_options=options) # 实例化带有配置的driver对象

driver.get(url)

print(driver.get_cookies())



cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}

print(cookies)

