### 5类容器都支持遍历其中列表 字符串 元组支持for 和 while
### 集合 和 字典 仅支持for

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = 'abcdefg'
my_set = {1,2,3,4,5}
my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}


### len
len(my_list)
len(my_tuple)
len(my_str)
len(my_set)
len(my_dict)
### max
max(my_list)
max(my_tuple)
max(my_str)
max(my_set)
max(my_dict)
### min
min(my_list)
min(my_tuple)
min(my_str)
min(my_set)
min(my_dict)

### 容器转列表
list(my_list)
list(my_tuple)
list(my_str)
list(my_set)
list(my_dict)

### 容器转元组
tuple(my_list)
tuple(my_tuple)
tuple(my_str)
tuple(my_set)
tuple(my_dict)

### 容器转字符串
str(my_list)
str(my_tuple)
str(my_str)
str(my_set)
str(my_dict)
del str

### 容器转集合
set(my_list)
set(my_tuple)
set(my_str)
set(my_set)
set(my_dict)

my_list = [5,4,3,2,1]
my_tuple = (5,4,3,2,1)
### 容器的通用排序功能 sorted(容器,reverse = True),返回值都是列表 函数不改变 而是拷贝一份 调用方法如果可变则变
sorted(my_list)
print(my_list)
sorted(my_tuple)
my_tuple
sorted(my_str)
sorted(my_set)
sorted(my_dict)
