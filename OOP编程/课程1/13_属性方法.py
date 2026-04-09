### 把一个方法变成一个静态的属性（变量）
# class Student(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def fly(self):
#         print(f"{self.name} is flying....")
#
# p = Student('lzx')
# p.fly()

### 我们的一个想法是把一个方法变成一个属性
class Student(object):

    def __init__(self,name):
        self.name = name
    @property ### 把实例方法变成了一个实力的属性可以用这个属性
    def fly(self):
        print(f"{self.name} is flying....")

p = Student('lzx')
p.fly### 看起来是个属性 实际上会执行一系列的动作


### 去哪网的逻辑
class FlightCheck(object):
    def __init__(self,flight_name):
        self.flight_name = flight_name
        # print(f"您正在查询航班号{self.flight_name}的状态....")

    def check_status(self):
        print("连接到航空公司api....")
        print(f"正在检查{self.flight_name}航班状态....")
        return 1

    @property
    def flight_status(self):
        status = self.check_status()
        if status == 0:
            print("航班取消")
        elif status == 1:
            print("航班到达")
        elif status == 2:
            print("航班已经起飞")
        else:
            print("不能确定航班状态")

    @flight_status.setter
    def flight_status(self,status):
        self.status = status### 绑定了 搞到实例空间了
        print("checking")

    @flight_status.deleter
    def flight_status(self):
        print("del....")



f = FlightCheck('CA888')
f.flight_status
f.flight_status = 1
print(f.status)
del f.status
