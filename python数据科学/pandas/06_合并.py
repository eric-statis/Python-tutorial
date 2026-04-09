### 合并 concatenate
import pandas as pd
import numpy as np
from pandas.io.formats import printing

df1 = pd.DataFrame(np.ones(shape=(3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.zeros(shape=(3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones(shape=(3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)

### 
df = pd.concat(objs=[df1,df2,df3],axis=0)
print(df)

df = pd.concat(objs=[df1,df2,df3],axis=0, ignore_index=True)
print(df)

# join功能
df1 = pd.DataFrame(np.ones(shape=(3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.zeros(shape=(3,4))*1,columns=['b','c','d','e'])
res = pd.concat(objs=[df1,df2],axis=0,join='inner',ignore_index=True)
print(res)

