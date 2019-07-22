import requests
'https://github.com/Adolph-Anthony'
'''
这样输入用户名密码访问
'''
r = requests.get('https://github.com/Adolph-Anthony', auth=('Adolph-Anthony', 'xujing518333'))
print(r.status_code)