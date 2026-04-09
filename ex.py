
import numpy as np
m1 = np.array([[1,2,3],
               [2,3,4]])
print(m1)
print(type(m1))
print(m1.ndim)
print(m1.shape)
print(m1.size)
print(m1.dtype)
m2 = np.array([[1,2,3],
               [2,3,4]],dtype = np.float32)
print(m2.dtype)

m3 = np.array([[1,2,3],
                [2,3,4],
                [4,5,6]])
a = np.zeros((10,1))
print(a)
### arange函数
print(np.arange(10))
a = np.arange(12)
b = a.reshape((3,4))
print(b)
a = np.random.randn(10)
print(a)
a.sort()
print(a)
a = np.linspace(0,10,20)
print(a)
a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
print(c)
c = a*np.sin(b)
print(c)
print(c<3)
print(c[c<3])
a = np.array([[1,2],
              [3,4]])
b = np.array([[2,2],
              [2,2]])
print(a*b)
print(a.dot(b))
print(a @ b)
a = np.random.random((2,4))
print(a)
print(np.max(a))
print(np.argmax(a))
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)
b = a[np.newaxis,:]
print(b)
print(b.shape)


a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)
b = a[:,np.newaxis]
print(b)
print(b.shape)

a = np.arange(10)
b = np.expand_dims(a, axis=0)
print(b)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])

five_up = (a >= 5)
print(five_up)
print(a[five_up])

divison_by2 = (a%2 == 0)
print(divison_by2)

condi = ((a>5) | (a<1))
print(condi)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.nonzero())
coordinate = list(zip(a.nonzero()[0],a.nonzero()[1]))
for i in coordinate:
    print(i)

print(a[a.nonzero()])

not_there = np.nonzero(a == 40)
print(not_there)


a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

a = np.array([1, 2, 3, 4])

c = a.sum()
print(c)

b = np.array([[1, 3], [1, 10]])
print(b.sum(axis=0))
print(b.sum(axis=1))

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x.flatten()