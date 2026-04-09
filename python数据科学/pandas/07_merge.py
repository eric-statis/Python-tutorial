from operator import le
import pandas as pd
import numpy as np

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
print(left)
print(right)
res = pd.merge(left = left,right = right,on = 'key')
print(res)
### consider two keys
left2 = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                      'key2':['K0','K1','K0','K1'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3']})
right2 = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                       'key2':['K0','K0','K0','K0'],
                       'C':['C0','C1','C2','C3'],
                       'D':['D0','D1','D2','D3']})
print(left2)
print(right2)
res = pd.merge(left = left2,right = right2,on = ['key1','key2'])
print(res)