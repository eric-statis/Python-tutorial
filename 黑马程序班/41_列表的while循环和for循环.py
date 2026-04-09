'''
既然数据容器可以存储多个元素，那么，就会有需求从容器内依次取出元素进行操作。
将容器内的元素依次取出进行处理的行为，称之为：遍历、迭代。

如何遍历列表的元素呢？
• 可以使用前面学过的while循环如何在循环中取出列表的元素呢？
• 使用列表［下标］的方式取出
循环条件如何控制？
•  定义一个变量表示下标，从0开始
• 循环条件为 下标值＜列表的元素数量

index = 0
while index < len(list):
    元素 = 列表[index]
    对元素进行处理
    index += 1
'''

def list_while_func(list):# while 无限循环
    index = 0
    while index < len(list):
        print(f"{list[index]}",end=' ')
        index += 1

### 复习使用while循环遍历列表
def while_list(list):
    index = 0
    while index < len(list):
        print(list[index])
        index += 1





list_while_func(['li','zong','xu'])

def list_for_func(list):# 有限循环
    for i in list:
        print(i,end=' ')
list_for_func(['li','zong','xu'])
