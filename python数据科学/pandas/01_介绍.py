from re import L
from turtle import pensize
from xmlrpc.client import FastMarshaller
import pandas as pd
import numpy as np
from regex import F
### 创建pandas 的序列
s = pd.Series(data=np.array([1,2,3,4,5]))
print(s)
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

### numpy叫做数组：一维数组，二维数组...
### pandas有一维序列，和dataFrame 下面进行dataframe形式的演示
dates = pd.date_range(start='20260216',periods=7)
print(dates)
####
data = pd.DataFrame(np.random.randn(7,4),index=dates,columns=['a','b','c','d'])
print(data)

df = pd.DataFrame(np.arange(12).reshape(3,4))
print(df)

### 还有一种方法
df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20220216'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})

print(df2)
### 属性
print(df2.dtypes)
print(df2.index)
print(df2.columns,'>>>>>')## 打印列名字
print(df2.values,">>>>>")## 每一行的数据
print(df2.describe())## 方法
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values(by='E'))