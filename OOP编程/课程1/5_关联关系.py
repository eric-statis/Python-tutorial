# # class Relationship:
# #     def __init__(self,p1,p2):
# #         self.couple = (p1.name,p2.name)
# #
# # class Person:
# #
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def do_priavte_stuff(self):
# #         pass
# #
# # p1 = Person('mjj')
# # p2 = Person('lyy')
# #
# # relation = Relationship(p1,p2)
# # print(relation.couple)
# # ####
# from tables import NaturalNameWarning
#
#
# class Relationship:
#     def __init__(self):
#         self.couple = ()
#     def make_couple(self,p1,p2):
#         self.couple = (p1,p2)### 重新赋值了属性
#         print(f"{self.couple[0].name}和{self.couple[1].name}是情侣")
#
# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def do_priavte_stuff(self):
#         pass
#
# p1 = Person('mjj')
# p2 = Person('lyy')
#
# relation = Relationship()
# relation.make_couple(p1,p2)
# print(relation.couple)
# relation.couple = ()
# print(relation.couple)
#
# # ####
# class Relationship:
#     def __init__(self):
#         self.couple = ()
#     def make_couple(self,p1,p2):
#         couple = (p1,p2)### local
#         print(f"{couple[0].name}和{couple[1].name}是情侣")
#
# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def do_priavte_stuff(self):
#         pass
#
# p1 = Person('mjj')
# p2 = Person('lyy')
#
# relation = Relationship()
# relation.make_couple(p1,p2)
# print(relation.couple)
#
# # ####
# class Relationship:
#     def __init__(self):
#         self.couple = ()
#     def make_couple(self,p1,p2):
#         self.couple = (p1,p2)###
#         return self.couple
# class Person:
#
#     def __init__(self,name):
#         self.name = name
#         self.relation = None
#
#     def do_priavte_stuff(self):
#         pass
#
# relation = Relationship()
# p1 = Person('mjj')
# p2 = Person('lyy')
# relation1 = relation.make_couple(p1,p2)
# print(relation1)
# p1.relation = relation1
# print(p1.relation)
#
#
# ###
# class RelationShip:
#     def __init__(self):
#         self.couple = []
#
#     def make_couple(self,obj1,obj2):
#         self.couple = (obj1,obj2)
#         print(f"{obj1.name}和{obj2.name}确定恋爱关系了")
#
#
# class Person:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         # self.partner = None
#
#     def do_private_stuff(self):
#         pass
#
#
# relation_obj = RelationShip()
#
# p1 = Person('mjj',24,'M')
# p2 = Person('lyy',22,'F')
#
# relation_obj.make_couple(p1,p2)### 成为对象
#
# ### 让每个人找到自己对象
# class RelationShip:
#     def __init__(self):
#         self.couple = []
#
#     def make_couple(self,obj1,obj2):
#         self.couple = (obj1,obj2)
#         print(f"{obj1.name}和{obj2.name}确定恋爱关系了")
#
#
# class Person:
#     def __init__(self,name,age,sex,relation):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.relation = relation
#         # self.partner = None
#
#     def do_private_stuff(self):
#         pass
#
#
# relation_obj = RelationShip()
# relation_obj.make_couple(p1,p2)### 成为对象
# p1 = Person('mjj',24,'M',relation_obj)
# p2 = Person('lyy',22,'F',relation_obj)
# print(p1.relation.couple)
### 没有打印出名字 怎么打印出对象的名字呢
class RelationShip:
    def __init__(self):
        self.couple = []

    def make_couple(self,obj1,obj2):
        self.couple = [obj1,obj2]
        print(f"{obj1.name}和{obj2.name}确定恋爱关系了")


class Person:
    def __init__(self,name,age,sex,relation: RelationShip):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation
        print(self)
        # self.partner = None
    def find_couple(self):
        for i in self.relation.couple:
            if i != self:
                print(f"找到对象了，对象是{i.name}")
                break
        else:
            print(f"{self.name}还没有对象")

    def do_private_stuff(self):
        pass

    def break_up(self):
        print("分手了")
        self.relation.couple.clear()

relation_obj = RelationShip()

p1 = Person('mjj',24,'M',relation_obj)
p2 = Person('lyy',22,'F',relation_obj)
relation_obj.make_couple(p1,p2)### 成为对象
p1.find_couple()
## 分手功能演示
p1.break_up()
p2.break_up()


