from re import A

from holoviews.plotting.bokeh.util import prop_is_none


class Dog:
    d_type = '京巴' # 属性 公共属性

    def __init__(self,name,age):### 私有属性
        print("hihihi",name,age)### 要把name和age这两个属性与实例绑定
        self.name = name### 绑定 d.name = name
        self.age = age

    ### 本质上上面下面两个函数是隔开的 但是通过绑定 在下面也可以调用了 因为默认把实例传入函数
    # 而实例和这些属性在构造方法绑定了 所以能调用


    def sayhi(self): #self是实例本身
        print(f"hello 我是{self.d_type},{self.name}")## 方法

d = Dog('mjj',3)
d2 = Dog('mjj2',4)
112344

111111


22

print(d.d_type)
print(d2.d_type)
d.sayhi()### 相当于d2.sayhi(d2) 所以需要把实例
'''
所以类属性，类变量，公共属性，所有实例共享实例属性，
实例变量，成员变量，每个实例独享
'''
### 属性引用之类属性调用
class Dog:
    d_type = '京巴' # 属性 公共属性

    def __init__(self,name,age):### 私有属性
        # print("hihihi",name,age)### 要把name和age这两个属性与实例绑定
        self.name = name### 绑定 d.name = name
        self.age = age

    ### 本质上上面下面两个函数是隔开的 但是通过绑定 在下面也可以调用了 因为默认把实例传入函数
    # 而实例和这些属性在构造方法绑定了 所以能调用


    def sayhi(self): #self是实例本身
        print(f"hello 我是{self.d_type},{self.name}")## 方法

print(Dog.d_type)#或者
d = Dog('mjj',2)
print(d.d_type)# 通过实例调用类属性

### 修改类的属性
Dog.d_type = '斑点'
print(Dog.d_type)# 现在类属性变成了斑点
print(d.d_type)

### 访问实例属性 实例属性只能通过实例调用不能通过类调用
print(d.name)

### 修改实例属性
d.name = 'mjj2'
print(d.name)

### 类属性不能访问实例属性
# print(Dog.name)

### 节省内存 所有的国籍都是CN 所以可以写成类属性
class People:
    def __init__(self,name, age, sex, nationality):
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality = nationality

p = People('mjj',22,'M','CN')
p = People('Alex',23,'M','CN')
p = People('Jack',25,'M','CN')

class People:
    nationality = 'CN'
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

p = People('mjj',22,'M')
p2 = People('Alex',23,'M')
p3 = People('Jack',25,'M')

print(p.nationality)
### mjj自己要改国籍直接在实例属性更改
p.nationality = 'USA'
print(p.nationality)
print(People.nationality)
'''
可以发现类属性是CN，但是mjj自己的属性是USA，因为p.nationality = 'USA'
相当于给p这个实例创建了实例属性 之前没创建 就会到类的内存空间找 现在找到
了 直接引用实例内存空间的实例属性
'''
