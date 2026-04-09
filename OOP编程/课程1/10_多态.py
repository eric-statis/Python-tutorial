'''有时一个对象会有多种表现形式，比如
网站页面有个button按钮，这个button的
设计可以不一样（单选框、多选框、圆角的点击按钮、
直角的点击按钮等），尽管长的不一样，但它们都有一
个共同调用方式，就是onClick（）方法。我们直要
在页面上一点击就会触发这个方法。点完后有的按钮会
变成选中状态、有的会提交表单、有的甚至会弹窗。这
种多个对象共用同一个接口，又表现的形态不一样的现象，
就叫做多态（Polymorphism）。
'''
### 第一种形式
class Dog(object):
    def sound(self):
        print("汪汪汪")

class Cat(object):
    def sound(self):
        print("喵喵喵")

def make_sound(obj):
    obj.sound()

d = Dog()
c = Cat()
make_sound(d)
make_sound(c)

### 利用抽象类写多态
class Document(object):
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'Show pdf contents'

class Word(Document):
    def show(self):
        return "Show word contents"

p = Pdf('真nb')
# p1= Word()
print(p.show())








