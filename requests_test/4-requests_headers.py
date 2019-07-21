
import requests

# 目标url
url = 'https://www.baidu.com'

# 发起请求
response = requests.get(url)
print(response.headers)
# 因为请求头中被识别不是正常浏览器所带的请求头
#
# print(len(response.content.decode()))
# print(response.content.decode())
# 以键值对构建请求头字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
# 发送带请求头的请求
response1 = requests.get(url,headers=headers)
print(len(response1.content.decode()))
print(response1.content.decode())
# print(response1.headers)
