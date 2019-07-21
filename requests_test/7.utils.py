import requests

# 目标url
url = 'https://www.baidu.com'

# 发起请求
response = requests.get(url)

print(response.cookies)

#
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)


# 因为后续的没能得到域名
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)