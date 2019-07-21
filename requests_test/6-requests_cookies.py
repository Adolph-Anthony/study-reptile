import requests
url = 'https://github.com/Adolph-Anthony'


headers = {
    'Cookie': '_octo=GH1.1.73506579.1538137739; _ga=GA1.2.1588836414.1538137744; _device_id=fad5ffb8a3d040a102353882883a84ed; user_session=vbcvPKjl1SaN25unnWZDF0ouw4BB3QmWbI4J23XQVEBwhWNS; __Host-user_session_same_site=vbcvPKjl1SaN25unnWZDF0ouw4BB3QmWbI4J23XQVEBwhWNS; logged_in=yes; dotcom_user=Adolph-Anthony; tz=Asia%2FShanghai; _gh_sess=dERCbURLQmZ2ODl5bkFXVjdOZ1cwZWRueXhWZllHb2V4L1pBZUk4bjFNUTJUUHJBY0QzRmhWTEh4TVZKVnJBK2Y2Uyt0RlU3QnJwRnBVc0ZFNzVVVlI4UHY2ZFNaNWtqSU1HWmxMNUpJc1V0OGJOSy9NM0duVnVkZ1lzMWVEaXRvcWVxR2FaTExRWkFoNWRVRlo1LzFzWUpybXNiVng5SC95L0NjK0NVUWhKbkJ6M2xldzFJRXY4RC9iY0laTmZXVlZxNk5jSWNlVG1jakRZZ05Jem80UnZPb0R4Z0RkUDF0N3NGaVVxQnk4M1ZmajZ0K3N2c3h1VTIzbFFhdHUxUElhQmNGWTZjZTZyUDNDbGdudDJJQ1BzSmRXSFd5QkNLdXVzRTJRNjFWUVFYcDFFY3BqSE1RNWpMSUFwbDVWN2EyUThvZlZMZGxxQ2NKQUJRRmdqdDlnPT0tLUlnbXBOemwyM2lzMU1SN0h1L1lTV0E9PQ%3D%3D--eb8fc3b519aa73f802b8587c25dc619a86958f44',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'


}
response = requests.get(url,headers = headers)
with open('github.html','wb') as f:
    # 发送带请求头的请求

    f.write(response.content)