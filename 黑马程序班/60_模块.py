'''
Python 模块（Module），是一个 Python 文件，以.py 结尾. 模块能定义函数，类和变量，模块里也能包含可执行的代码.
'''
### 使用import
import time# 导入python内置的time.py文件 摁住ctrl点击即可进入这个文件
print("你好")
print("我好")
time.sleep(2)

### from 模块名 import 功能

### from 模块名字 import * 导入全部功能
from time import *
sleep(2)

### 加上as相当于起了个别名

### 导入自定义模块
from functions import func
func.test()
func.my_add(1, 3)


from functions import func
func.a

from functions.func import my_add
my_add(1,3)

from functions.utilis import my_add

my_add(1,2)
