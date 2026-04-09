### 可以通过字符串操作实例属性
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print("walking")
p = Person('lzx',30)
### 有时候我们其他地方用这个类时 我们不知道这个类里面到底有没有某个属性
### hasattr反射 映射 自省
if hasattr(p,'name'):
    print("NB")

# hasattr
# getattr
# setattr
# delattr

### getattr
a = getattr(p,'age')
print(a)

### hasattr
# user_input = input("请输入指令：")
# if hasattr(p,user_input):
#     func = getattr(p,user_input)
#     func()

### setattr 设置一个属性
setattr(p,'sex','F')
print(p.sex)

### 设置一个方法
## 写一个方法
def bark(self):
    print(f"{self.name}正在呐喊")
setattr(Person,'bark',bark)
# p.bark(p)# TypeError: bark() takes 1 positional argument but 2 were given 传了实例又传了self
# p.bark(p)

### delattr
delattr(Person,'bark')
# p.bark()

print(__name__)
if __name__ == '__main__':### 这里会打印__main__ 其他文件文件导入会打印fanshe
    # 所以在当前文件内 main == main  没问题 打印hahaha
    print('hahaha')

###
import sys
print(sys.modules.items())
print(sys.modules['__main__'])