'''
函数有四种常见的传参方式
位置参数
关键字参数
缺省参数
不定长参数
位置参数：调用函数时根据函数定义的参数位置来传递参数必须按照定义函数的参数位置进行传参

关键字参数：使用键值匹配的方式进行传参数，在这种情况下可以把顺序打乱

当位置参数和关键字参数混用时，必须把位置参数作为第一个，同时关键字部分的参数顺序仍然可以打乱

缺省参数：在函数值中设置默认值，如果不传递参数，就使用默认值，如果传递参数，就按照所传递的参数，默认值必须是最后一个参数。

不定长参数：不定长参数也叫做可变参数，用于不确定调用的时候会传递多少参数（也有可能不传递参数）。当不确定参数个数时，应该使用不定长参数。可以细分为位置传递，关键字传递 

位置传递：*args >>> tuple
def user_info(*args):
    print(args) 

关键字传递：**kwargs >> dict
def user_info(**kwargs):
    print(kwargs)    
user_info('name' = 'Tom','age' = 19)
'''

def user_info(name, age, gender):
    print(f"姓名是{name}，年龄是{age}，性别是{gender}。")
user_info('lizongxu',20,'男')

user_info(age=20,gender='男',name='lizongxu')

### 缺省参数
def user_info(name, age, gender = '男'):
    print(f"姓名是{name}，年龄是{age}，性别是{gender}。")

user_info(20,'lizongxu')

user_info(20,'lizongxu','女')

### 不定长
def user_info(*args):
    print(f'{args}的类型是{type(args)}')
user_info('Tom')

def user_info(**kwargs):
    print(f'{kwargs}的类型是{type(kwargs)}')
user_info(name = 'Tom',age = 19)
