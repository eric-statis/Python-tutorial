'''
• def关键字，可以定义带有名称的函数
•lambda关键字，可以定义匿名函数（无名称）
有名称的函数，可以基于名称重复使用，可以调用。无名称的匿名函数，只可临时使用一次。

lambda 传入参数：函数体（一行代码）
lambda 是关键字，表示定义匿名函数
• 传入参数表示匿名函数的形式参数，如：x，y表示接收2个形式参数
• 函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
'''
def test_func(compute):
    result = compute(1,2)
    return result

def compute(x,y):
    return x+y
'''
上述就是
lambda x,y: x+y
'''

test_func(lambda x,y: x+y)# lambda不需要return直接返回 没办法二次使用调用这个函数 因为没有名字


### 做一个计算器函数
def compute(input):
    args = tuple(input)
    i = 0
    for j in args:
        i = j + i
    return i

compute(input("输入数字："))

def compute(numbers):
    i = 0
    for i in numbers:
        i += i 
        return i
    
user_input = input("请输入，输入示例: 1.2,3.5:")
try:
    compute([float(x) for x in user_input.split(',')])
except ValueError:
    print("111")

