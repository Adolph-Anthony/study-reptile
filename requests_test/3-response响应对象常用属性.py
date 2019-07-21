import requests

# 目标url
url = 'https://www.baidu.com'

# 发起请求
response = requests.get(url)


print(response.url)                            # 打印响应的url
print(response.status_code)                    # 打印响应的状态码
print(response.request.headers)                # 打印响应对象的请求头
print(response.headers)                        # 打印响应头
print(response.request._cookies)               # 响应对应请求的cookie；返回cookieJar类型
print(response.cookies)                        # 响应的cookie（经过了set-cookie动作；返回cookieJar类型（dict or list）