import requests

# 目标url
url = 'https://www.twitter.com'

# 发起请求
response = requests.get(url,timeout = 3)

