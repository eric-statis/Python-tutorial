class Person:
    def __init__(self,name,age,sex):
        self.age = age
        self.sex = sex
        self.name = name

        print(self.__dict__)### 实例属性 以字典传递

    def __len__(self):
        print(f"{self.name}的长度是")
        return  1
    def __hash__(self):
        print('hahahah')
        return  1
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass


p = Person('lzx',30,"M")
# print(len(p))
# print(hash(p))
print(p['name'])
# print(p.__getattr__('sex'))