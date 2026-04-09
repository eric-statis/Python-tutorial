class Dog:
    role = '狗'

    def __init__(self,
                 name:str,
                 breed:str,
                 attack_val:int):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self,
             person):
        person.life_val -= self.attack_val
        print(f"狗{self.name}，咬了人{person.name}，掉血{self.attack_val}，还剩{person.life_val}。")


### 人狗大战 的 OOP版本
class People:
    role = '人'

    def __init__(self,
                 name,
                 attack_val,
                 sex):
        self.name = name
        self.attack_val = attack_val
        self.sex = sex
        self.life_val = 100

    def attack(self,
               dog: Dog):
        dog.life_val -= self.attack_val
        print(f'人{self.name}打了狗{dog.name}，狗掉血{self.attack_val}，还剩{dog.life_val}')

d1 = Dog('mjj','二哈',20)
d2 = Dog('吗金毛','金毛',40)
p1 = People('Alex',60,'M')
p1.attack(d1)
d1.bite(p1)



class Dog:
    role = '狗'

    def __init__(self,
                 name:str,
                 breed:str,
                 attack_val:int,
                 life_val = 100):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = life_val

    def bite(self,
             person):
        person.life_val -= self.attack_val
        print(f"狗{self.name}，咬了人{person.name}，掉血{self.attack_val}，还剩{person.life_val}。")


### 人狗大战 的 OOP版本
class People:
    role = '人'

    def __init__(self,
                 name,
                 attack_val,
                 sex,
                 life_val = 100):
        self.name = name
        self.attack_val = attack_val
        self.sex = sex
        self.life_val = life_val

    def attack(self,
               dog: Dog):
        dog.life_val -= self.attack_val
        print(f'人{self.name}打了狗{dog.name}，狗掉血{self.attack_val}，还剩{dog.life_val}')

d1 = Dog('mjj','二哈',20,200)
d2 = Dog('吗金毛','金毛',40)
p1 = People('Alex',60,'M')
p1.attack(d1)
d1.bite(p1)
'''
类与类之间的关系
大千世界，万物之间皆有规则和规律.我们的类和对象是对大千世界中的所有事物进行归类.那事物之间存在着相对应的关系.类与类之间也同样如此.在面向对象的世界中，类与类中存在以下关系：
1. 依赖关系，狗和主人的关系
2. 关联关系，你和你的女盆友的关系就是关联关系
3. 组合关系，比聚合还要紧密.比如人的大脑，心脏，各个器官.这些器官组合成一个人.这时.人如果挂了.其他的东西也跟着挂
了
4.聚合关系，电脑的各部件组戒完整的电脑，电脑里有CPU，硬盘，内存等。每个组件有自己的生命周期，电脑挂了．CPU还是好的.还是完整的个体
5.继承关系，类的三大特性之一，子承父
'''