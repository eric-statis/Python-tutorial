'''
在程序中是可以做到和生活中那样，设计表格、生产表格、填写表格的组织形式的

设计表格：设计类
class Student()

打印表格: 创建对象
stu_1 = Student()
stu_2 = Student()

填写表格: 为对象赋值
stu_1.name =  ’周杰伦'
stu_2.name =  '林俊杰'
'''

### 设计类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

### 创建对象
stu_1 = Student()

### 对对象赋值
stu_1.name = '林俊杰'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '山东省'
stu_1.age = 31

### 获取记录的信息
print(stu_1.name)

###