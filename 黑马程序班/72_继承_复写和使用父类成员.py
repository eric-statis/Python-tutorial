'''
复写：
子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。即：在子类中重新定义同名的属性或方法即可 Child定义同名属性 和 方法

调用父类的同名成员：
一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员如果需要使用被复写的父类的成员，需要特殊的调用方式

方式1
调用父类成员
使用父类的成员变量：父类名.成员变量
使用父类的成员方法：父类名.成员方法(self)

方式2
使用super()调用
super().成员方法()
super().成员变量



子类就是继承父类 定义一个重名成员相当于复写了 但是你在这个子类中要用父类的咋整 都被复写了 如果直接用self.成员和方法()是子类自己的
通过Phone.成员变量 Phone.call_by5g(self)






'''
class Phone:
    producer = '黑马'
    def call_by5g(self):
        print('父类的5g通话')

class MyPhone(Phone):
    producer = '苹果' ### 复写
    def call_by5g(self):
        print("子类的5g通话")

phone = MyPhone()
phone.call_by5g()
phone.producer
'''
>>> phone.call_by5g()
子类的5g通话
>>> phone.producer
'苹果'
'''

### 使用父类的成员
class Phone:
    IMEI = None
    producer = 'ITCAST'

    def call_by5g(self):
        print("使用5g网络进行通话")

class MyPhone(Phone):
    producer = 'ITHEIMA'
    name = Phone.producer
    '''
    name = super().producer不对 super方法只在子类方法中用
    '''
    # def call_by5g(self):
    #     return Phone.call_by5g(self)
    # def call_by5gA(self):
    #     return Phone.call_by5g(self)
    
phone = MyPhone()
phone.name
phone.call_by5gA()

### method1
class Phone:
    IMEI = None
    producer = 'ITCAST'

    def call_by5g(self):
        print("使用5g通话")
class MyPhone(Phone):
    producer = 'ITHEIAM'        
    def  call_by5g(self):
        print("开启CPU单核模式，确保通话时省电")
        super().call_by5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by5g()

### method1
class Phone:
    IMEI = None
    producer = 'ITCAST'

    def call_by5g(self):
        print("使用5g通话")
class MyPhone(Phone):
    producer = 'ITHEIAM'        
    def  call_by5g(self):
        print("开启CPU单核模式，确保通话时省电")
        Phone.call_by5g(self)
        print(f"父类的生产商为{Phone.producer}")
        print(f"子类的生产商是{self.producer}")
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by5g()



### method2
class Phone:
    IMEI = None
    producer = 'ITCAST'

    def call_by5g(self):
        print("使用5g通话")
class MyPhone(Phone):
    producer = 'ITHEIAM'        
    def  call_by5g(self):
        print("开启CPU单核模式，确保通话时省电")
        super().call_by5g()
        print(f"父类的生产商为{super().producer}")
        print(f"子类的生产商是{self.producer}")
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by5g()

### 在子类使用父类的方法
class Parent:
    def greet(self):
        print("Parent: Hello")
    
    def introduce(self):
        print("I am Parent")

class Child(Parent):
    def greet(self):
        # 调用父类同名方法（扩展行为）
        super().greet()          # ✅ 推荐
        print("Child: Hi there!")
    
    def show(self):
        # 调用父类其他方法
        super().introduce()      # ✅ 推荐

c = Child()
c.greet()
# 输出:
# Parent: Hello
# Child: Hi there!

c.show()
# 输出: I am Parent