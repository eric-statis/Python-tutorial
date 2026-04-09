### json与python数据格式转换
import json
data = [{"name":'张大山','age':11},{'name':'王大锤','age':13},{'name':'赵小虎','age':16}]
### python转化为d
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))

d = {'name': '周杰伦','age':18}

d_json = json.dumps(d,ensure_ascii=False)
### json to python dict or list
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
json.loads(s)