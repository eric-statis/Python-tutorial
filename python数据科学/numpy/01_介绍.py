import numpy as np


m1 = np.array([[1,2,3],
               [2,3,4]]) ### 数组
print(m1)

print(f'dim of m1 is {m1.ndim}')### 属性
print(f"shape of m1 is {m1.shape}")
print(f"size of m1 is {m1.size}")

###
a = np.array([[1,23,4]])

a = np.array([1,23,4],dtype=np.float32)
print(a)
print(a.dtype)

m = np.array([[1,2,3],
              [2,3,4],
              [3,4,5]])
print(m)

m = np.zeros((3,4))
print(m)


m = np.ones((3,4))
print(m)


a = np.empty((3,4))
print(a)

print(np.arange(0,10)[-3:-1])
print(np.arange(1,10,2))
a = np.arange(0,12)
b = a.reshape((3,4))
print(b)

b = a.sort()
print(b)

# a = np.linspace(1,10,20)
# print(a)
