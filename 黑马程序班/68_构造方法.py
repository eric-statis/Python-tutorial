'''
class Student:
    name = None
    age = None

    def say_hello(self):
        print(f"大家好，我是{self.name}")

stu_1 = Student()

stu_1.name = '周杰伦'
stu_1.age = 20
stu_1.say_hello()
上册代码中，在传入属性时，需要以此进行比较繁琐

stu_1 = Student()### 传参的方式传入对象的属性，通过__init__()

• 在创建类对象（构造类）实例化的时候，会自动执行。
• 在创建类对象（构造类）的时候，将传入参数自动传递给_init__方法使用。
'''
#### 构造方法的名称: __init__
class Student:

    def __init__(self,name:str, age:int, tel:int):### 构造方法

        self.name = name### 构造方法依然是一个方法 在方法中使用成员属性依然需要使用self
        self.age  = age
        self.tel = tel
        print("Student类创建了一个对象")

# stu = #Student('周杰伦',20,110)
# print(stu.age)
'''
Student类创建了一个对象 因为在实例化时 构造方法自动执行
'''

### 练习题目
class Student_info:

    def __init__(self, name:str, age:int, address: str):
        self.name = name
        self.age = age
        self.address = address
        print("信息录入")
 
students = []

for i in range(10):
    name = input("您的姓名是：")
    age = int(input("您的年龄是:"))
    address = input("您的住址是：")
    students.append(Student_info(name, age, address))


for i in range(10):
    print(f"第{i}位学生的住址是{students[i].address}")
