### 对象后面加括号触发执行
class School(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(self,args,kwargs)

### 实例化
s = School('lzx')
s('nihao','hello',nishi = 'xiaowang')
