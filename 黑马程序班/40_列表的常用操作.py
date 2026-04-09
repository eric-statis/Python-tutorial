### 如果将函数定义为class的成员此时就不称作函数 而是称之为一个方法
def add(x,y):
    return x+y
###
class Student:
    def add(x,y):
        return x+y

add(1,2)
Student()
Student.add(1,2)
## .代表方法

### 查找指定元素的下标.index(元素)
my_list = ['itcasst','itheima','python']
my_list.index('itheima')
my_list.index('hello')

### 改
my_list[0] = 'hello'
print(my_list)

### 增

my_list.insert(0,'my_python')## 在指定位置插入元素
my_list

### 追加

my_list.append('Li')
my_list

### 追加多个元素

my_list_2 = [1,2,3]
my_list.extend(my_list_2)
print(my_list)

### 删除的用法del 、 pop方法
my_list = ['itheima','itcast','python']
del my_list[0]
print(f"删除之后的列表为{my_list}")

my_list = ['itheima','itcast','python']
element = my_list.pop(0)
print(f"删除后的列表为{my_list}，删除的元素为{element}")

### 通过remove方法移除特定元素
my_list = ['itheima','itheima','itheima','itcast','python']
my_list.remove('itheima')
print(f"通过remove方法移除之后的列表为{my_list}")

### 通过clear方法清空列表
my_list = ['itheima','itcast','python']
my_list.clear()
print(f"清空之后的列表是{my_list}")

### 列表内某一个元素的数量
my_list = [1,2,3,3,34,4,5]
my_list.count(3)

### 列表元素的数量 函数
len(my_list)

