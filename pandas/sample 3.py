# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:12:32 2020

@author: 16132
"""
import pandas as pd 
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
print(df.dropna(axis=1,how = 'any')) #drop the row if there are any 'nan' in this row
#how = {'any','all'}  how = all,means if all the element in this row/column are nan, drop this row/column
print(df.fillna(value=0))# fill nan using other value
print(df.isnull()) # judge the element in the dataframe equals to nan or not 
print(np.any(df.isnull()) == True) #at least one element is nan