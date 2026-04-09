### 装饰器@classmethod 使得方法只能访问类变量：储存在类中 不能访问实例变量：储存在实例空间中
class Dog(object):
    def __init__(self,name):
        self.name = name

    @classmethod# 装饰器
    def eat(self):
        print(f"{self.name}")

d = Dog('mjj')
# d.eat() AttributeError: type object 'Dog' has no attribute 'name'
###

class Dog(object):
    name ='stupid dog'### 类变量
    # def __init__(self,name):
    #     self.name = name

    @classmethod
    def eat(self):
        print(f"{self.name}")

d = Dog()
d.eat()

# d.eat() AttributeError: type object 'Dog' has no attribute 'name'


###

class Dog(object):
    name ='stupid dog'### 类变量
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print(f"{self.name}在吃东西")

d = Dog('mjj')
d.eat()
# 实际传入的是类本身 虽然是self但实际上传入的不是实例
class Dog:
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(cls):
        print(cls)

d = Dog('mjj')
d.eat()




'''为什么不是mjj在吃东西，我们看一下使用类方法和不用类方法 self到底是谁'''
class Dog(object):
    name ='stupid dog'### 类变量
    def __init__(self,name):
        self.name = name
        print('--->',self)

    @classmethod
    def eat(self):# self不是实例对象 而是类本身因此常用cls与self区分
        print('--->',self)
        print(f"{self.name}在吃东西")

d = Dog('mjj')
d.eat() #不传d 传的是Dog这个类本身因此只能拿到类变量！！！
'''
---> <__main__.Dog object at 0x10546e510>
---> <class '__main__.Dog'> 类本身
'''


### 写一个人员报道的类
class People(object):
    count = 0
    def __init__(self,
                 name,
                 age,
                 sex):
        self.name = name
        self.age = age
        self.sex = sex
        People.count += 1
        print(f"人员报道人员数量为{People.count}")

p1 = People('lzx',30,"M")
p2 = People('Alex',20,"F")
### 保护内部变量不被外部访问
class People(object):
    __count = 0
    def __init__(self,
                 name,
                 age,
                 sex):
        self.name = name
        self.age = age
        self.sex = sex
        People.__count += 1
        print(f"人员报道人员数量为{People.__count}")

p1 = People('lzx',30,"M")
p2 = People('Alex',20,"F")

### 使用类方法;
class People(object):
    __stu_num = 0
    def __init__(self,name):
        self.name = name
        self.__add_stu()

    @classmethod
    def __add_stu(cls):
        cls.__stu_num += 1
        print(f"数量为{cls.__stu_num}")

p1 = People('lzx')
### 判断要不要计数
class People(object):
    __stu_num = 0
    def __init__(self,name):
        self.name = name
        self.add_stu(self)### self就是实例本身

    @classmethod
    def add_stu(cls,obj):### obj ### cls是类本身
        if obj.name:
            cls.__stu_num += 1
        print(f"学院数量为{cls.__stu_num}")

p1 = People('lzx')
# People.add_stu(1)

