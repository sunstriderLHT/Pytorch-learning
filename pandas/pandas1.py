# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:12:38 2020

@author: 16132
"""

import pandas as pd
import numpy as np
#构建
s=pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20200101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=['a','b','c','d']) #pd.DataFrame(数据，行标签，列标签)
print(df)
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'}) #通过字典构建df
print(df2)
print(df2.dtypes) #输出数据类型
print(df2.index) #输出行标签
print(df2.columns) #输出列标签
print(df2.values) #输出元素
print(df2.describe()) #输出统计信息  只能计算数字
print(df2.T) #转置
print(df2.sort_index(axis=1,ascending=False)) #axis=1排序列，ascending=False倒序
print(df2.sort_values(by='E')) #按照某一列排序