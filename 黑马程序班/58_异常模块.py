'''
当检测到一个错误时，Python解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的“异常”，也就是我们常说的BUG当检测到一个错误时，Python解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的“异常”，也就是我们常说的BUG
'''
### 通过open打开一个不存在的文件
open('linux.txt',mode='r')
'''
>>> open('linux.txt',mode='r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'linux.txt'
'''

'''
我们要做的，不是力求程序完美运行。
而是在力所能及的范围内，对可能出现的bug，进行提前准备、提前处理。

当我们的程序遇到了BUG，那么接下来有两种情况：
① 整个程序因为一个BUG停止运行
② 对BUG进行提醒，整个程序继续运行

显然在之前的学习中，我们所有的程序遇到BUG就会出现①的这种情况，也就是整个程序直接奔溃.
但是在真实工作中，我们肯定不能因为一个小的BUG就让整个程序全部奔溃，也就是我们希望的是达到② 的这种情况那这里我们就需要使用到捕获异常，保证程序能够正常运行，不再报错

捕获异常的作用在于：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段。

基本语法
try:
    可能发生问题的代码
except:
    如果错误执行的代码
'''
###：尝试以r模式打开文件，如果文件不存在，则以w方式打开。
try:
    open('./txt/linux.txt',mode='r',encoding='utf-8')
except:
    print("出现异常了！")
    open('./txt/linux.txt',mode='w',encoding='utf-8').flush()
'''
捕获指定的异常
try:
    print(name)
except NameError as e:
    print("由于名字所引起的异常")
'''
### 指定捕获的异常
try:
    print(name)
except NameError as e:
    print("变量未定义的异常")
    print(e)


try:
    1/0
except NameError as e:
    print("变量未定义的异常")
    print(e)

### 捕获多个异常
try:
    1/0
    print(name)
except (NameError,ZeroDivisionError):
    print("出现了错误")

### 捕获所有异常 一共两种和直接except一样
try:
    1/0
    print(name)
    open('./txt/nizhenqiang.txt',mode='r')
except Exception as e:
    print(e)
    print("出现异常")

### 没有异常else用法
try:
    print('hello')
except:
    print("出现异常")
else:
    print("没有异常被捕获")

### final 无论是否出现异常都执行
try:
    f = open('./txt/123.txt',mode='r')
except:
    print("不存在此文件")
    f = open('./txt/123.txt',mode='w')
else:
    print("真开心没异常")
finally:
    print("程序保存")
    f.close()