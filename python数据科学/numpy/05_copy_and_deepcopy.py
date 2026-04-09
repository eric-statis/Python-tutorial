import numpy as np
### 列表
a = [0,1,2,3]
b = a
c = a
d = b
print(a,b,c,d)
a[0] = 11
print(a,b,c,d)###
### [11, 1, 2, 3] [11, 1, 2, 3] [11, 1, 2, 3] [11, 1, 2, 3]也是都改了
print(id(a),id(b),id(c),id(d))# 5111709760 5111709760 5111709760 5111709760


### 上述在python中称为浅层复制
print(b is a)

### array
a = np.arange(4)
b = a 
c = a
d = b
print(a,b,c,d)
a[0] = 11
print(a,b,c,d)
###[11  1  2  3] [11  1  2  3] [11  1  2  3] [11  1  2  3]很奇怪吧都改了
### 上述在python中称为浅层复制
print(b is a)
print(d is a)


############ deep copy 不发生关联
a = np.arange(4)
b = a.copy()
print(b is a)