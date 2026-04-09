import pandas as pd
import numpy as np
from pyparsing import col
from regex import D
from sympy import print_maple_code
from xlrd import colname

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[2,2] = 1111
print(df)

df.loc['20130101','C'] = 2222
print(df)
#
df.loc[df.loc[:,'A']<20,'A'] = 0
print(df)
#
df['E'] = pd.Series([1,2,3,4,5,6],index=dates)
print(df)