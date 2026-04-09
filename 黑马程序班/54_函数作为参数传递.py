'''
在前面的函数学习中，我们一直使用的函数，都是接受数据作为参数传入：
• 数字
• 字符串
• 字典、列表、元组等
其实，我们学习的函数本身，也可以作为参数传入另一个函数内。
'''

### 一个小例子 函数作为参数传递
def compute(x,y):
    return x + y, x-y
    

def test_func(x,y,compute = compute):
    result = compute(x,y)
    return result

test_func(3,2)[1]

### 
def test_func(compute):
    result = compute(1,2)
    print(f"compute的类型是{type(compute)}")
    print(f"计算的结果是{result}")

def compute(x,y):
    return x+y# 函数返回值

test_func(compute)






### 一个小例子 函数作为参数传递
def compute(x,y):
    return x + y, x-y
    

def test_func(x,y,compute2 = compute):
    result = compute2(x,y)
    return result

test_func(1,2)


def compute_1(x,y):
    return x+y, x-y

def test_funcc(x,y):
    result = compute_1(x,y)
    return result  

test_funcc(1,2)