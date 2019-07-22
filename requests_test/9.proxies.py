import requests
url = 'http://www.baidu.com'
# 发起请求
# response = requests.get(url)

proxies = {
    'http':'http://115.218.215.236:9000'
    # 'https':'http://121.232.194.111:9999',

}
response = requests.get(url,proxies=proxies)

print(response.content.decode())
