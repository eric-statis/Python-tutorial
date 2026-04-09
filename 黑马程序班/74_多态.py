###
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

cat = Cat()
dog = Dog()
def make_noise(animal: Animal):
    animal.speak()
make_noise(cat)
make_noise(dog)    


#######
class Cat():
    def speak(self):
        print("喵喵喵")

class Dog():
    def speak(self):
        print("汪汪汪")

cat = Cat()
dog = Dog()
def make_noise(animal):
    animal.speak()
make_noise(cat)
make_noise(dog)    

### 抽象类
'''
抽象类的设计可以用父类确定有哪些方法 具体的方法实现有子类决定

含有抽象方法的类是抽象类

抽象方法的实现是pass Animal

类似一个标准
'''
### 定义一个抽象类 标准设计
class AC:
    '''制冷'''
    def cool_wind(self):
        pass
    
    '''制热'''
    def hot_wind(self):
        pass

    def swing_l_r(self):
        '''左右摆风'''
        pass


class Gree_AC(AC):
    def cool_wind(self):
        print("美的")

    def hot_wind(self):
        print("美的")

    def swing_l_r(self):
        print("美的")   

class Media_AC(AC):
    def cool_wind(self):
        print("格力")

    def hot_wind(self):
        print("格力")

    def swing_l_r(self):
        print("格力")   

def make_cool(ac: AC):
    ac.cool_wind()        

ac1 = Media_AC()
ac2 = Gree_AC()

make_cool(ac1)
make_cool(ac2)