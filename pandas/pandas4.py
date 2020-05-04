# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:16:49 2020

@author: 16132
"""

import pandas as pd
import numpy as np

dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

print(df.dropna(axis=0,how='any'))  # how = {'any','all '} 只要有nan删除行
print(df.dropna(axis=1)) #how默认为any，丢掉含nan的列

print(df.fillna(value=0))  #用特定值填充NaN

print(df.isnull(),'\n')  #缺失数据的位置为True

print(np.any(df.isnull()) == True) #至少有一个位置为True就输出True

