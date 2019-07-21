import requests

# 目标url
url = 'https://www.baidu.com'

# 向目标url发送get请求
response = requests.get(url)

# response.encoding = 'utf8'
# print(response.text)
# 存储bytes类型的响应源码,可以decode
print(response.content.decode())
'''
response.text是requests模块按照chardet模块推测出的编码字符集进行解码的结果
网络传输的字符串都是bytes类型的，所以response.text = response.content.decode('推测出的编码字符集')
我们可以在网页源码中搜索charset，尝试参考该编码字符集，注意存在不准确的情况'''

'''

response.text
类型：str
解码类型： requests模块自动根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码

response.content
类型：bytes
解码类型： 没有指定
'''