# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:19:26 2020

@author: 16132
"""
import pandas as pd
import numpy as np
#赋值
dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df,'\n')
df.iloc[2,2] = 111
df.loc['20200102','A'] =222
print(df)
#df1=df[df.A>4] = 0 #把A标签数据大于4的行元素变为0
#print(df1)
df.B[df.A>4] = 0 #把A标签数据为大于4的B行元素变为0
print(df)
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20200101',periods=6))
print(df)