# 掌握 requests模块发送get请求
import requests

# 目标url
url = 'https://www.baidu.com'

# 发起请求
response = requests.get(url)

print(response.text)