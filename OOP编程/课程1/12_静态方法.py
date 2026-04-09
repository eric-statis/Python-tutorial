class Student(object):
    role = 'Stu'

    def __init__(self,name):
        self.name = name
    @staticmethod
    def fly(self):
        print(f"{self.name}正在飞")
    @staticmethod
    def walk():# 不会自动写self 因为隔断 要是写上self你就得自己传入
        print("跑步进行")
s1 = Student('lzx')
# s1.fly() Student.fly() missing 1 required positional argument: 'self'
s1.fly(s1)## 可以 这是为啥 调用方法 不是自动传吗s1.fly(s1)
### 因为静态方法隔离了 他和类和实例的任何关系