import numpy as np


a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
# print(c)
print(b)
print(b**2)
c = a*np.sin(b)
print(c)

### 判断
print(c<3)### 有返回值
print(c[c<3])
###
a = np.array([[1,2],
              [3,4]])
b = np.array([[2,2],
              [2,2]])
c = a*b
d = np.dot(a,b)
print(c)
print(d)

a = np.random.random((2,4))
print(a)
print(np.max(a))
print(np.argmax(a))
print(np.max(a,axis=1))
print(np.argmax(a,axis=1))
print(np.max(a,axis=0))
print(np.argmax(a,axis=0))

print(np.sort(a))
print(a.T.dot(a))