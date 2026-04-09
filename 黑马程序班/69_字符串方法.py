'''
__str__



'''
### 创建一个类
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
student = Student('周杰伦', 20)
print(student)
print(str(student))
'''
当类对象需要被转换为字符串之时，会输出如上结果（内存地址）
>>> print(student)
<__main__.Student object at 0x101189890>
>>> print(str(student))
<__main__.Student object at 0x101189890>
内存地址没有多大作用，我们可以通过_str_方法，控制类转换为字符串的行为。
'''
### 使用__str__方法 打印
class Student:
    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age
    def __str__(self):
        return f"student类对象，name = {self.name}，年龄是{self.age}。"

student = Student('林俊杰', 30)
print(str(student))

### 使用__lt__魔术方法进行大小比较；le；eq
class Student:
    ### 构造方法
    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age
    ### 打印方法
    def __str__(self):
        return f"student类对象，name = {self.name}，年龄是{self.age}。"
    ### 比较方法 只能判断大于和小于不等判断小于等于或者大于等于
    def __lt__(self,other):
        return self.age < other.age

    ### le 方法判断小于等于或者大于等于
    def __le__(self,other):
        return self.age <= other.age 
    
    ### eq 方法判断是否相等
    def __eq__(self,other):
        return self.age == other.age

student1 = Student('林俊杰', 30)
student2 = Student('周杰伦', 40)
print(student1 > student2)
student1 < student2
student1 >= student2
student1 == student2