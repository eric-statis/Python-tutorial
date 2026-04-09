### 单继承
# parent
class Phone:
    IMEI = 12211
    producer = '黑马'

    def call_by4g(self):
        print("4g通话已开启")

# Child 继承父类的属性和方法
class Phone2022(Phone):
    face_id = True

    def call_by5g(self):
        print("5g通话已开启")

phone = Phone2022()
phone.IMEI
phone.producer
phone.face_id    
phone.call_by4g()
phone.call_by5g()


### 多继承 一个子类child 继承parent1 parent2 ...
class NFC_reader:
    nfc_type = None
    producer = "黑马"

    def read_card(self):
        print("NFC读卡")
    
    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = None

    producer = '黑马'

    def control(self):
       print("红外遥控开启") 
    

class MyPhone(Phone,NFC_reader,RemoteControl):
    pass### 不添加

phone = MyPhone()
phone.IMEI


### MRO机制
class Phone:
    producer = "华为"  # 修改为不同值

class NFC_reader:
    producer = "小米"

class RemoteControl:
    producer = "苹果"

class MyPhone(Phone, NFC_reader, RemoteControl):
    pass

phone = MyPhone()
print(phone.producer)  # 输出: 华为（MRO 第一个匹配）Phone优先 同名优先级 同名成员 














