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
               dog):
        dog.life_val -= self.attack_val
        print(f'人{self.name}打了狗{dog.name}，狗掉血{self.attack_val}，还剩{dog.life_val}')


class Dog:
    role = '狗'

    def __init__(self,
                 name:str,
                 breed:str,
                 attack_val:int,
                 master: People):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100
        self.master = master#### 对象
    def sayhi(self):
        print(
            f"大家好我是{self.name},我的主人是{self.master.name}"
        )





    def bite(self,
             person):
        person.life_val -= self.attack_val
        print(f"狗{self.name}，咬了人{person.name}，掉血{self.attack_val}，还剩{person.life_val}。")

p1 = People("Alex",10,'M')
Dog('mjj','金毛',10,p1).sayhi()