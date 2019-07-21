# coding:utf-8
# import requests
#
# # 目标url
# url = 'https://www.baidu.com/s?wd=python'
#
#
# # 以键值对构建请求头字典
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
# # 发送带请求头的请求
# response = requests.get(url,headers=headers)
# with open('baidu.html','wb') as f:
#     f.write(response.content)
import requests

# 目标url
url = 'https://www.baidu.com/s?'


# 以键值对构建请求头字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
# 构建参数字典
data = {
    'wd':'python'

}



response = requests.get(url,headers=headers,params=data)

print(response.url)

with open('baidu1.html','wb') as f:
    # 发送带请求头的请求

    f.write(response.content)