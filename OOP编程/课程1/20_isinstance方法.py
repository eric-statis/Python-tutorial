### 检查某个东西是是不是某个类实例化出的
from regex import D


class School(object):
    def __init__(self,
                 name):
        self.name = name

s = School('lzx')
print(isinstance(s,School))

class Dog(object):
    def __init__(self,
                 name):
        self.name = name
    