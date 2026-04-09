import os
import numpy as np
import pandas as pd
df = pd.read_csv('python数据科学/pandas/data/student.csv')
print(df)
df.to_pickle('python数据科学/pandas/data/student.pkl')