'''
思考：列表是可以修改的。
如果想要传递的信息，不被篡改，列表就不合适了。
元组同列表一样，都是可以封装多个、不同类型的元素在内。
但最大的不同点在于：
元组一旦定义完成，就不可修改
所以，当我们需要在程序内封装数据，又不希望封装的数据被篡改，那么元组就非常合适了
'''

### 定义元组字面量
(1,'lizongxu','3')
### 定义变量
t1 = (1,'lizongxu','3')
t2 = ()
t2 = tuple()
print(f"t1的类型是{type(t1)}")

### 定义只有一个元素的tuple要注意加,
t3 = ('hello',)
t4 = ('hello')
print(f"t3的类型是{type(t3)},t4的类型是{type(t4)}")# t3的类型是<class 'tuple'>,t4的类型是<class 'str'>

### 元组的嵌套
t5 = (1,2,(1,2,3))
type(t5)

### 元组支持查和索引
t5[2][1]

'''
tuple由于不可修改的特性，方法比较少
'''
### 
t5 = ('传智教育','黑马程序员','Python')
t5.index('传智教育')
###

t5.count('传智教育')
###
len(t5)


### 元组的循环while for
def while_tuple(tuple):
    index = 0
    while index < len(tuple):
        print(f"元素{tuple[index]}",end=' ')
        index += 1
while_tuple(t1)
### 
def for_tuple(tuple):
    for i in tuple:
        print(i)
for_tuple(t1)
t1[0] = 2# TypeError: 'tuple' object does not support item assignment
### 可以修改元组内的list的内容（修改元素、增加、删除、反转等)
t9 = ([1,2,3,4],['li','zong','xu'])
t9[1][1] = 'hello'
print(t9)# ([1, 2, 3, 4], ['li', 'hello', 'xu'])
t9[1].pop(0)
print(t9)

### 联系题目
t = ('周杰伦',11,['football','music'])
t.index(11)
t[0]
del t[2][0]
print(t)