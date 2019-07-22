import requests
# 忽略CA证书
url = 'https://sam.huat.edu.cn:8443/selfservice/'

response = requests.get(url,verify= False)