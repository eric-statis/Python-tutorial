### 函数化
from torch.ao.quantization import default_weight_fake_quant


def dog(name: str, type: str, attack_val: int, life_value: int):
    data = {
        'name': name,
        'type': type,
        'attack_val': attack_val,
        'life_value': life_value
    }
    return data

d1 = dog(name='mjj',type = '京巴', attack_val = 30, life_value= 100)

### 根据类型自动赋值
attack_val = {
    '京巴': 30,
    '藏獒': 100
}
def dog(name: str, type: str, life_value = 100) -> dict:
    attack_val_inner = None
    if type in attack_val.keys():
        attack_val_inner = attack_val[type]
    else:
        pass
    data = {
        'name': name,
        'type': type,
        'attack_val': attack_val_inner,
        'life_value': life_value
    }
    return data
dog('mjj','京巴')

def person(name: str,age: int,life_value = 100) -> dict:
    data={
        'name':name,
        'age':age,
        'life_value':life_value,
        'attack_val':None
    }
    if age >= 18:
        data['attack_val'] = 50
    else:
        data['attack_val'] = 10
    return  data

d1 = dog('mjj','京巴')
print(d1)
p1 = person('李宗旭',30)
print(p1)

def dog_bite(dog_obj: dict,person_obj:dict) -> None:
    print(f"狗{dog_obj['name']}，咬了人{person_obj['name']}，掉血{dog_obj['attack_val']}")

# dog_bite(d1,p1)
# dog_bite(p1,d1)
'''这样做无法避免上述问题'''

### 解决办法1
def dog(name: str, type: str, life_value = 100) -> dict:
    if type in attack_val.keys():
        attack_val_inner = attack_val[type]
    else:
        pass
    data = {
        'name': name,
        'type': type,
        'attack_val': attack_val_inner,
        'life_value': life_value,
        'bite':None
    }

    def dog_bite(person_obj):
        person_obj['life_value'] -= data['attack_val']
        print(f"狗{data['name']}，咬了人{person_obj['name']}，掉血{data['attack_val']}，还剩生命值{person_obj['life_value']}")

    data['bite'] = dog_bite

    return data


dog('mjj','京巴')['bite'](p1)

### 可以编写人打狗函数
def person(name:str,age:int,life_value = 100):
    if age >= 18:
        attack_val = 50
    else:
        attack_val = 10
    data = {
        'name': name,
        'age': age,
        'life_value':life_value,
        'attack_val': attack_val
    }
    def person_hit(dog_obj:dict):
        dog_obj['life_value'] -= data['attack_val']
        print(
            f"人{data['name']}，打了狗{dog_obj['name']}，掉血{data['attack_val']}，还剩生命值{dog_obj['life_value']}")

    data['bite'] = person_hit
    return data
person('李宗旭',30)['bite'](d1)
person('李宗旭',30)['bite'](d1)
person('李宗旭',30)['bite'](d1)


p1 = person('李宗旭',30)
p2 = person('小子',30)
d1 = dog('mjj','京巴')
p1['bite'](d1)
### 你再看一下前面写的dog 和 person其实就是一个类啊
'''
你在设计角色时，为了让一个角色可以变成多个实体对象，你设计了一个基础模板，只要传入不同参数，就会产生不同的狗。这代表你已经开始切换成上帝视角看事情，上帝视角就是面向对象编程的视角，上帝要造世界万物，他肯定不是一个一个的造出来，他肯定是设计出一个个的物种的模板，然后通过模子批量批一个个的实体造出来。造出来的实体各有特色，属性、功能都不尽相同，有的人的贪婪、有的人好色、有的人懦弱，有的人勇猛。这些人之间会发生什么关系，谁和谁交媾、谁和谁打仗，上帝懒的管，上帝只控制大局。听着玄乎吧，我们接下来一点点接晓怎么通过面向对象在编程世界里做上帝。
'''