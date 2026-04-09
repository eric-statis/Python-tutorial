'''
类的基本语法
class 类名称:
    类的属性：成员变量，定义在类中变量叫做属性

    类的行为：成员方法，定义在类中的函数叫做方法

创建类的语法
对象 = 类名称()

在类中定义成员方法和定义函数基本一致，但仍有细微区别：
def 方法名（self，形参1，••••••，形参N）：
方法体
可以看到，在方法定义的参数列表中，有一个：self关键字self关键字是成员方法定义的时候，必须填写的。
• 它用来表示类对象自身的意思
• 当我们使用类对象调用方法的是，self会自动被python传入
• 在方法内部，想要访问类的成员变量，必须使用self
'''

class Student:
    name = None
    age = None

    def say_hello(self):
        print(f"大家好，我是{self.name}")

stu_1 = Student()

stu_1.name = '周杰伦'
stu_1.say_hello()

###
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}") ### 在方法中使用属性必须使用self

    def say_hi2(self,msg:str):
        print(f"大家好，我是{self.name},{msg}")### 使用name是成员属性要想使用必须使用self，但是msg是外部传入的不需要self

stu = Student()
stu.name = '周杰伦'### 传入属性
stu.say_hi()### 调用方法
stu.say_hi2('nb')


stu_2 = Student()
stu.name = '林俊杰'
stu.say_hi()