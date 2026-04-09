import numpy as np
import pandas as pd
dates =pd.date_range('20220216',periods=7)
df = pd.DataFrame(data=np.random.randn(7,4),index=dates,columns=['A','B','C','D'])
print(df)

### 筛选
print(df['A'],df.A)
print(df[0:3],df['20220219':'20220222'])### 对行进行筛选
# select by label: loc
print(df.loc['20220222',['A','B']])
print(df.loc[:,['A','B']])
# select by position: iloc
print(df.iloc[[1,2,3],:])

# select by boolean
print(df)
print(df[df.A < 0.1])

print(df)
print(df.loc[df.A<0.1,['A','B']])