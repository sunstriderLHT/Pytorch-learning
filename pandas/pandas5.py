# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:25:50 2020

@author: 16132
"""
#存取
import pandas as pd
import numpy as np

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

res = pd.concat([df1,df2,df3],axis=0,ignore_index = True) #改变行数，并重新记录列序号
print(res)

# join, ['innner','outer']
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)

res = pd.concat([df1,df2])  #默认为outer 将两者合并用NaN填充没有的部分
print(res)

res = pd.concat([df1,df2],axis=0, join='inner',ignore_index=False)  #inner将两者都有的部分合并
print(res)

#join axes
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])

res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)

#append
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'],index=[2,3,4])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'],index=[2,3,4])
res=df1.append([df2,df3],ignore_index=True)

print(res)

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])

res=df1.append(s1,ignore_index=True)

print(res)












