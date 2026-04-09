import numpy as np

A = np.arange(3,15)
B = A.reshape(3,4)
print(B)
print(B[0])
print(B[0,2])
print(B[2:])
print(B[0,0:2])
### 迭代行
for row in B:
    print(row)

### 迭代列
for col in B.T:
    print(col)

### 迭代元素
print(B.flatten())
for i in B.flatten():
    print(i)