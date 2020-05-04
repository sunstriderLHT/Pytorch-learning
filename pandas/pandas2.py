# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:53:09 2020

@author: 16132
"""

import pandas as pd 
import numpy as np
#筛选
dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df,'\n')
print(df['A'],'\n') #输出A列元素
print(df.A,'\n')
print(df[0:3],'\n')
print(df['20200101':'20200103'],'\n')

#select by label:loc
print(df.loc['20200101'],'\n')
print(df.loc[:,'A':'C'],'\n') #输出A列到c列所有元素
print(df.loc['20200103',['A','B']],'\n') #输出行标签为20200103，列标签为A或B的元素

#select by position: iloc
print(df.iloc[3,1],'\n') #输出第四行第二列
print(df.iloc[3:5,1:3],'\n')

#Boolean indexing
print(df[df.A>8],'\n') #条件判断筛选


data = np.random.randint(10,20,size=20).reshape(4,5)
df2 = pd.DataFrame(data)
print(df2[df2>15])
