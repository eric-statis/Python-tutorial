####
class Person(object):
    def __init__(self,name,age):
        self.age = age
        self.name = name

p = Person('lzx',30)
print(type(p))
print(type(Person))# <class 'type'>

### 使用type创建一个类
dog_class = type("Dog",(object,),{'type':'dog','breed':'金毛'})
print(dog_class)
### 实例化 包含类变量
dog = dog_class()
print(dog.type)
### 包含构造方法
def __init__(self,name,age):
    self.name = name
    self.age = age

dog_class = type("Dog",(object,),{'role':'狗','breed':'金毛','__init__':__init__})
dog = dog_class('lzx',20)
print(dog.name)
print(dog.age)