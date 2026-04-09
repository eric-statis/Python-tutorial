#
my_str = 'itheima and itcast'
#索引
my_str[0]
# index方法
my_str.index('and')
### 注意字符串是不可变数据类型，不能够修改，定义一个新字符串
my_str[2] = 'H'
## 字符串的replace方法 不是修改字符串本身，而是得到了一个返回一个新字符串
new_str = my_str.replace('it','程序')
print(new_str)
### split ：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中 字符串本身不变，而是得到了一个列表对象
str = 'ni hao hello world'.split(' ')
str
### strip方法 这个方法是有参数的 不填有默认值，传了按你的
def add_method(x = 0,y = 5):
    return x + y
add_method()# 有默认值的函数 add_method() 5
my_str = '  itheima  '
new = my_str.strip()
print(f'原来是{my_str}，修改之后是{new}')
### 统计字符中中字符中的出现次数
my_str = 'itheima and itcast'
my_str.count('i')
# 统计长度
len(my_str)
### 同列表、元组一样，字符串也支持while循环和for循环进行遍历 只要可以查就可以遍历
def while_str(str):
    index = 0
    while index < len(str):
        print(str[index])
        index += 1
while_str('ithema')

'''
给定一个字符串：mitheimaitcast boxuegui
•统计字符串内有多少个量“it"字符
• 将字符串内的空格，全部替换为字符：|
• 并按照"“进行字符串分割，得到列
'''
str = 'mitheimaitcast boxuegui'
str.count('it')
new = str.replace(' ','|')
newnew  = new.split('|')
print(newnew)