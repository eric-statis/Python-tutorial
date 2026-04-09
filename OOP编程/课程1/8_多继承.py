class ShenXian:
    '''神仙类'''
    def fly(self):
        print("神仙都会飞")

class Monkey:
    '''猴子类'''
    def eat_peach(self):
        print("猴子都会吃桃子")

class MonkeyKing(ShenXian,Monkey):
    def play_golden_stick(self):
        print("孙悟空会玩金箍棒")

m = MonkeyKing()
m.fly()
m.eat_peach()
m.play_golden_stick()

### 顺序
class ShenXian:
    '''神仙类'''
    def fly(self):
        print("神仙都会飞")

    def fight(self):
        print("神仙打架")


class Monkey:
    '''猴子类'''
    def eat_peach(self):
        print("猴子都会吃桃子")

    def fight(self):
        print("猴子会打架")

class MonkeyKing(ShenXian,Monkey):
    def play_golden_stick(self):
        print("孙悟空会玩金箍棒")

m = MonkeyKing()
m.fly()
m.eat_peach()
m.play_golden_stick()
m.fight()

### 菱形继承查找顺序
class Base:
    def fight(self):
        print("动物会打架")

## 左边
class MonkeyBase(Base):
    # def fight(self):
    #     print("猴子始祖在打架")
    pass
class Monkey(MonkeyBase):
    # def fight(self):
    #     print("猴子在打架")
    pass

## 右边
class ShenXianBase(Base):
    def fight(self):
        print("神仙始祖在打架")

class ShenXian(ShenXianBase):
    def fight(self):
         print("神仙在打架")

## 子类
class MonkeyKing(Monkey,ShenXian):
    # def fight(self):
    #     print("孙悟空在打架")
    pass
## 实现
m = MonkeyKing()
m.fight()
print(MonkeyKing.mro())
'''
[<class '__main__.MonkeyKing'>, <class '__main__.Monkey'>, 
<class '__main__.MonkeyBase'>, <class '__main__.ShenXian'>, 
<class '__main__.ShenXianBase'>, <class '__main__.Base'>, <class 'object'>]

'''

















