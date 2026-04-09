### new方法在__init__之前
from bokeh.core.property.instance import Object


class School(object):

    def __init__(self,
                 name):
        self.name = name
        print('hahaha')
    def __new__(cls, *args, **kwargs):
        ### new方法在构造方法之间 执行构造方法这里可以看成重写了
        print(cls,*args,kwargs)
s = School('lzx')

'''
<class '__main__.School'> lzx {}
Traceback (most recent call last):
  File "/Users/lixiansheng/Desktop/Python基础学习/OOP编程/课程1/17_new方法.py", line 12, in <module>
    s.name
AttributeError: 'NoneType' object has no attribute 'name'
'''
### 要想成功使用构造方法 要调用父类方法
class School(object):

    def __init__(self,
                 name):
        self.name = name
        print('hahaha')
    def __new__(cls, *args, **kwargs):### 可以进行一些初始化之前的工作
        ### new方法在构造方法之间 执行构造方法这里可以看成重写了 不会执行构造方法了
        print(cls,*args,kwargs)
        return super().__new__(cls)
        return Object.__new__(cls)### 都可以 cls是显示参数
s = School('lzx')


### __new__方法的使用 打印机任务
class Printer(object):
    task = []
    def __init__(self,name):
        self.name = name

    def add_task(self,job):
        Printer.task.append(job)
        print(f"{self.name}添加任务到打印机，当前总任务数量{len(Printer.task)}")

###
p1 =  Printer('word')
p2 = Printer('pdf')
p3 = Printer('excel')
p1.add_task('word file')
p2.add_task('pdf file')
p3.add_task('excel file')
print(p1,p2,p3)
### 这里存在问题是如果我实例化多个 地址不一样
### 自动长度
# def fuck(*args):
#     for i in args:
#         print(f"fuck {i}")
#
# fuck('lzx','leilei','nihao')
# ###
# def fuck(**kwargs):
#     for i in kwargs:
#         print(kwargs[i])
#
# fuck(lzx = 30,lili = 30)
#
#
### 高级用法
class Printer(object):
    task = []
    instance = None
    def __init__(self,name):### 实例初始化
        self.name = name
        print("构造方法执行")

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            #构建实例
            cls.instance = super().__new__(cls)### 创建实例
            print(f"返回{cls.instance}")### 只有当 __new__ 返回当前类（cls）或其子类的实例时动调用 __init__
        return cls.instance


p1 = Printer('word')
p2 = Printer('pdf')
print(p1,p2)# <__main__.Printer object at 0x107a05950> <__main__.Printer object at 0x107a05950>
print(p1.name,p2.name)# 都是pdf














