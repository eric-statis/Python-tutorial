'''
OOP:面向对象编程，是许多编程语言都支持的一种编程思想。
简单理解是：基于 模板（类）去创建实体（对象），使用对象完成功能开发。

面向对象编程的三大特性：
封装 
多态
继承 

### 封装：
封装表示的是，将现实世界事物的：
• 属性
• 行为
封装到类中，描述为：
• 成员变量
• 成员方法
从而完成程序对现实世界事物的描述

### 私有成员
既然现实事物有不公开的属性和行为，那么作为现实事物在程序中映射的类，也应该支持。
类中提供了私有成员的形式来支持。
• 私有成员变量
• 私有成员方法、
定义私有成员的方式非常简单，只需要：
• 私有成员变量：变量名以_开头（2个下划线） >>>>>私有变量无法赋值，也无法获取值
• 私有成员方法：方法名以_开头（2个下划线） >>>>>私有方法无法直接被类对象使用
即可完成私有成员的设置

可以被类中其他成员使用，公开的成员会使用私有的成员
'''
### 定义一个类其中蕴含私有成员变量和私有成员方法
class Phone:
    __current_voltage = None

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

phone = Phone()
phone.__current_voltage
'''
>>> phone.__current_voltage
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Phone' object has no attribute '__current_voltage'. Did you mean: '_Phone__current_voltage'?
'''
phone.__keep_single_core()
'''
>>> phone.__keep_single_core()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Phone' object has no attribute '__keep_single_core'. Did you mean: '_Phone__keep_single_core'?
'''
### 使用私有成员
class Phone:
    __current_voltage = 2

    def __keep_single(self):
        print("手机单核运行")

    def call_by_5g(self):
        if self.__current_voltage < 1:
            self.__keep_single()
        else:
          print("5G模式开启")
phone =Phone()
phone.call_by_5g()

### 练习题
class Phone:
    
    __is_5g_enable = True
    
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")
    
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()