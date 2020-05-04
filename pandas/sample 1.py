# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:49:42 2020

@author: 16132
"""
import pandas as pd
import numpy as np
print('pandas statistic selection')
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print('输出行标签为A的列： ')
print(df['A'])
print(df.A)
print('\n输出第0-2行：')
print(df[0:3])
print('\n输出行标签为20130102到20130104的行')
print(df['20130102':'20130104'])
print('*'*40)


print('\n select by label: loc')
print(df.loc['20130102'])
print('\n select by index and columns label')
print(df.loc['20130102',['A','B']])
print('*'*40)

print('\n select by position: iloc')
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
print('*'*40)


print('\n mixed selection: ix')
print(df.ix[:3,['A','C']])
print('*'*40)

print('\n select based on bool')
print(df[df.A>8]) #when the element in column A >8 print the row

