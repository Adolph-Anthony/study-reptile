import requests
import json
import sys

class King(object):
    def __init__(self,word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.word = word
        self.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        self.data = {
            "f":"auto", # 表示被翻译的语言是自动识别
            "t":"auto",# 表示翻译后的语言是自动识别
            "w": word # 要翻译的中文字符串
        }


    def get_data(self):
        # 使用post方法发送一个post请求,data为请求体的
        response = requests.post(self.url,data = self.data,headers = self.headers)
        # print(type(response.content))
        return response.content

    def prase_data(self,data):
        # loads方法将json字符串转换成python字典
        dict_data = json.loads(data.decode())
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])


    def run(self):
        # 编写爬虫逻辑

        # url
        # headers
        # data字典
        # 发送请求,获取响应
        response = self.get_data()
        self.prase_data(response)
        # print(response)
        # 数据解析
if __name__ == '__main__':
    # word = input("请输入要翻译的单词或句子:")
    word = sys.argv[1]
    king = King(word)
    king.run()