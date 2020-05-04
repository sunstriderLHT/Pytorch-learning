# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:50:10 2020

@author: 16132
"""
print('change element in the dataframe')
import pandas as pd 
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2] = 1111
df.loc['20130101','B'] = 2222
#df[df.A>4] = 0  if element of column A >4, change the element of this row to 0
df.A[df.A>4] = 5 #if element of column A >4, change this element in column A to 5 (only change A)
df.B[df.A>4] = 6 #if element of column A >4, change the element in column B in this row to 6 (only change B)
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods =6 ))

print(df)
