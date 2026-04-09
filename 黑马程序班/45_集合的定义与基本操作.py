'''
我们目前接触到了列表、元组、字符串三个数据容器了。基本满足大多数的使用场景。

一些特性：是否有序（查），是否可以重复，是否可以修改（增删改）

通过特性来分析：
• 列表可修改、支持重复元素且有序
• 元组、字符串不可修改、支持重复元素且有序同学们，有没有看出一些局限？

支持重复和有序 如果场景需要对内容做去重处理，列表、元组、字符串就不方便了 
集合不支持重复 而且是无序的（无法查）但是集合和列表一样，是允许修改的，所以我们来看看集合的修改方法。
''' 
### 定义集合
a = {1,2,3,4}
a = set()
### 不能用{} 空字典
{'传智教育','黑马程序员','itheima'}
my_set = {'传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima'}
my_set_empty = set()
### 增加一个新元素add
my_set.add('Python')
print(my_set)
my_set.add('传智教育')
print(my_set)

### 删除指定元素remove 方法有参数
my_set = {'传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima'}
my_set.add('Python')
my_set.remove('Python')

### pop方法 功能由于集合无序不支持索引 不用指定参数 随机取一个作为返回值 同事集合被修改该元素被移除
my_set = {'传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima','传智教育','黑马程序员','itheima'}
pop_ele = my_set.pop()
print(pop_ele)
my_set

### 清空集合
my_set.clear()

### 集合的运算 差集 两个集合都不会发生变化
A = {1,2,3}
B = {2,3,4}
A.difference(B)

### 在集合A删除B的元素 集合A发生变化 B发生变化
A.difference_update(B)
A

### 并集 两个集合都不会发生变化
A.union(B)

### 统计集合中的元素数量len
len(A)

### 集合不能够索引不能查 不能使用while循环 只能使用for循环
def for_set(set):
    for i in set:
        print(i)