import numpy as np

A = np.array([1,1])
B = np.array([2,2])
C = np.vstack((A,B))
print(C)
D = np.hstack((A,B))
print(D)

a = np.array([1,1,1])
print(a.shape)
print(a.T)
print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)
print(a[np.newaxis,:].T.shape)
####
a = np.array([1,1,1])[np.newaxis,:]
b = np.array([2,2,2])[np.newaxis,:]
print(a)
print(b)
print(np.vstack((a,b)))
print(np.concatenate((a,a,b,b),axis=0))