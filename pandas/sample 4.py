# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:04:33 2020

@author: 16132
"""
import pandas as pd
import numpy as np 
# pandas read and write function

data = pd.read_csv('student.csv')
print(data)

data.to_pickle('student.pickle')

print('*'*40)

#pandas combine dataframe
# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#垂直方向合并，忽略原始序号重新生成序号
print(res)

# join,['inner','outer']
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index = [1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index = [2,3,4])