### 组合关系：由一堆组件构成一个完整的实体，
# 组件本身独立，但又不能自己运行，必须跟宿主组合在一起，运行
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


class People:
    role = '人'

    def __init__(self,
                 name,
                 attack_val,
                 sex,
                 life_val = 100):
        self.name = name
        # self.attack_val = attack_val
        self.weapon = Weapon()
        self.sex = sex
        self.life_val = life_val

    def attack(self,
               dog: Dog):
        dog.life_val -= self.attack_val
        print(f'人{self.name}打了狗{dog.name}，狗掉血{self.attack_val}，还剩{dog.life_val}')

class Weapon:
    '''
    Person组件类：
    使用不同的武器进行攻击
    '''
    def stick(self,target):
        self.name = '打狗棒'
        self.attack = 40
        target.life_val -= self.attack
        self.print_log(target)

    def knife(self,target):
        self.name = '屠龙刀'
        self.attack = 80
        target.life_val -= self.attack
        self.print_log(target)

    def gun(self,target):
        self.name = 'AK47'
        self.attack = 100
        target.life_val -= self.attack
        self.print_log(target)

    def print_log(self,target):
        print(f"{target.name}被{self.name}攻击了，掉血{self.attack}")
p = People('Alex',30,'M')
d1 =  Dog('mjj','金毛',20)

print(id(p.weapon))## <__main__.Weapon object at 0x104f8a910>
p.weapon.gun(d1)
print(p.weapon.name)###
print(id(Weapon))
print(p.name)
'''

'''

# class W:
#     def stick(self, target):
#         self.name = '打狗棒'
#         self.attack = 40
#         # target.life_val -= self.attack
#
#
# ww = W()
# ww.stick('lll')
# print(ww.name)### 建立一个实例属性存在ww