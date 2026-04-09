from conda.notices.views import print_more_notices_message


class Animal:
    def __init__(self,
                 name,
                 age,
                 sex):
        self.name = name
        self.age = age
        self.sex = age

class People(Animal):
    ### 为什么没有构造方法？？？？？？？
    #### 有的孩子 继承了Animal中的构造函数明白了吧
    def walk(self):
        print(f"People{self.name}走路")

class Pig(Animal):
    def eat(self):
        print(f"Pig{self.name}吃东西")

class Dog(Animal):
    def bark(self):
        print(f"Dog{self.name}咬人")

person = People('李宗旭',30,'M')
person.walk()
pig = Pig("Mjj",4,"M")
pig.eat()
dog = Dog("毛毛",3,"F")
dog.bark()
'''
继承的有点也是显而易见的：

1，增加了类的耦合性。

2，减少了重复代码。

3，使得代码更加规范化，合理化。

继承的分类
就向上面的例子：

Aminal 叫做父类,基类,超类。

Person Pig Dog: 子类，派生类。

继承：可以分单继承，多继承。
'''

### 上述继承 继承实例的属性和方法 比如我想在人里面增加一些属性
class Animal:
    def __init__(self,
                 name,
                 age,
                 sex):
        self.name = name
        self.age = age
        self.sex = age

class People(Animal):
    def walk(self):
        print(f"People{self.name}走路")



### 重写构造方法
class Animal:
    type_breed = '金毛'
    def __init__(self,
                 name,
                 age,
                 sex):
        self.name = name
        self.age = age
        self.sex = age

class People(Animal):
    # def __init__(self,name,age,sex):
    #     super().__init__(name,age,sex)### 在子类方法调用父类方法

    def __init__(self,name,age,sex,race):### 重写父类的构造方法 建议使用超类调用父类的方法和属性
        Animal.__init__(self,name,age,sex)### 在子类使用父类方法 使用构造方法
        self.race = race### 增加子类的属性


    def print_log(self):
        print(f"父类中有属性{super().type_breed}")

animal1 = Animal('alex',2,'M')

p = People('lzx',30,'M',"chinese")
print(p.race)
print(p.name)

### 继承父类的方法&重构
class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        pass


class People(Animal):
    def __init__(self,name,age,sex,race):
        super().__init__(name,age,sex)# 调用父类方法
        self.race = race

    def walk(self):
        print(f"人{self.name}会走路")

class Pig(Animal):
    def __init__(self,name,age,sex,weight):
        super().__init__(name,age,sex)
        self.weight = weight
    def eat(self):
        print("爱吃")

pig = Pig('zhu',10.,"F",100)
print(pig.eat())

###
class Animal:
    ### 构造函数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = sex
        self.sex = sex
    def eat(self):
        print("动物要吃东西")

class Person(Animal):
    a_type = '人类'
    def eat(self):
        print(f'{self.name}爱吃肉')
p = Person('李宗旭','29','M')
p.eat()
### 不完全重写的思路而是先执行父类 在执行子类实现子类方法上的增加
class Animal:
    ### 构造函数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = sex
        self.sex = sex
    def eat(self):
        print("动物要吃东西")

class Person(Animal):
    a_type = '人类'
    def eat(self):
        super().eat()
        print(f'{self.name}爱吃肉')
p = Person('李宗旭','29','M')
p.eat()
### 重写构造方法
class Animal:
    ### 构造函数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = sex
        self.sex = sex
    def eat(self):
        print("动物要吃东西")

class Person(Animal):
    a_type = '人类'
    def __init__(self,name):
        self.name = name

    def eat(self):
        super().eat()
        print(f'{self.name}爱吃肉')
p = Person('李宗旭')
p.eat()
#### 不完全重写构造方法 而是增加
class Animal:
    ### 构造函数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = sex
        self.sex = sex
        print("父类运行")
    def eat(self):
        print("动物要吃东西")

class Person(Animal):
    a_type = '人类'
    def __init__(self,name,age,sex,weight):
        super().__init__(name,age,sex)
        self.weight = weight
        print("子类运行")

    def eat(self):
        super().eat()
        print(f'{self.name}{self.weight}斤爱吃肉')
p = Person('李宗旭',20,'M',100)
p.eat()




























