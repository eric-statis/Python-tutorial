### 定义一个字典 
{'wanglihong': 99,'zhoujielun': 88,'linjunjie': 77}
my_dict = {'wanglihong': 99,'zhoujielun': 88,'linjunjie': 77}
my_dict2 = {}
print(f"my_dict的类型是{type(my_dict)}")

### 字典的key不允许重复！！！ {}
my_dict3 = {'wanglihong': 99,'zhoujielun': 88,'linjunjie': 77, 'linjunjie': 77}
print(my_dict3)

### 和集合一样不能索引 因此不能通过索引查 但是可以通过key查
my_dict['linjunjie']### 但类似索引
my_dict['wanglihong']

'''
字典的Key和Value可以是任意数据类型（Key不可为字典）那么，就表明，字典是可以嵌套的需求如下：记录学生各科的考试信
'''
score = {
    '王力宏':{
        '语文':99,
        '数学':100,
        '英语':100},
    '周杰伦':{
        '语文':19,
        '数学':20,
        '英语':100
    },
    '林俊杰':{
        '语文':100,
        '数学':100,
        '英语':100
    }
}
print(score)
### 周杰伦的语文
score['周杰伦']['语文']
