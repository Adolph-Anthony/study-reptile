import requests
import re
def login():
    # session
    session = requests.session()
    # headers
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # '<input type="hidden" name="authenticity_token" value="JbApgg39wKze4KWFapPilXK8vIlQBTksxwTI/jjmb6FjJy7OdfriDqPeORR48XAN+MaF7nl6UXyfb7HJ6NlXtw==">'
    # url-获取token
    url1 = 'https://github.com/login'
        # 发送请求 获取响应
    res1 = session.get(url1).content.decode()
        # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />',res1)[0]
    print(token)
    # url2-登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        "commit": "Sign in",
        "utf8": "✓",
        "authenticity_token": token,
        "login": "1137847433@qq.com",
        "password": "xujing518333",
        "webauthn-support": "supported"
    }
    # print(data)
    # 发送请求登录
    session.post(url2,data=data)
    # url3-验证
    url3 = 'https://github.com/Adolph-Anthony'
    response = session.get(url3)
    print(response.status_code)
    with open('git.html','w') as f:
        f.write(response.content.decode())
if __name__ == '__main__':

    login()