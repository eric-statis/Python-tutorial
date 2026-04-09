'''
OOP面向对象：基于类创建对象的语法：对象名 = 类名称（）为什么非要创建对象才能使用呢？
类只是一种程序内的“设计图纸”，需要基于图纸生产实体（对象），才能正常工作
'''
### 设计闹钟
class Clock:
    clock_id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

### 生产闹钟
clock_1 = Clock()
clock_1.clock_id = '003032'
clock_1.price = 19.99
clock_1.ring()
print(f"闹钟id是{clock_1.clock_id}，价格是{clock_1.price}")
