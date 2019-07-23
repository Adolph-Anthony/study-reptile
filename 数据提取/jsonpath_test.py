from jsonpath import jsonpath

data = {'key1':{'key2':{'key3':{'key4':'python'}}}}

# print(data['key1']['key2']['key3']['key4'])

# jsonpath的结果为列表,获取数据需要索引
print(jsonpath(data,'$.key1.key2.key3.key4')[0])
print(jsonpath(data,'$..key4')[0])