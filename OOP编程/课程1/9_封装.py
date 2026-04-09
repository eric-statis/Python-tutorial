from pasta.base.annotate import space_left


class Person(object):
    ### 构造方法
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__life_val = 100### 这种数据不应该被访问 应该转化为私有属性 内部可使用
        '''类属性 实例属性 实例方法 私有属性 私有方法'''
    def get_val(self):
        print(f"{self.__life_val}")

###
p = Person('李宗旭',20,'M')
# print(p.__life_val) AttributeError: 'Person' object has no attribute '__life_val'
p.get_val()

### 上述例子只能访问不能够修改 下面做一个可以进行修改的例子
class Person(object):
    ### 构造方法
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__life_val = 100### 这种数据不应该被访问 应该转化为私有属性 内部可使用
        '''类属性 实例属性 实例方法 私有属性 私有方法'''
    def get_val(self):
        print(f"{self.__life_val}")

    def got_attack(self):
        self.__life_val -= 20
        print("被攻击了")
        self.__breathing()
        return self.__life_val

    def __breathing(self):
        print(f"{self.name}正在呼吸")

p = Person('李宗旭',20,'M')
print(p.got_attack())
print(p.got_attack())
### 非要访问也可以
p._Person__breathing()
