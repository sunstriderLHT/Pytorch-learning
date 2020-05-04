# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:51:39 2020

@author: 16132
"""

import pandas as pd

# merging two df key
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

res = pd.merge(left,right,on='key') #基于key 合并
print(res)

# consider two keys

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})


# how = ['left','right','inner','outer']
res = pd.merge(left,right,how='inner',on=['key1','key2'])  # how 默认为inner,只合并相同部分
print(res,'\n')

res = pd.merge(left,right,how='outer',on=['key1','key2'])  #outer 全部合并没有的项用NaN填充
print(res,'\n')

res = pd.merge(left,right,how='right',on=['key1','key2']) #right 按照right的key合并
print(res,'\n')

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

# indicator 显示如何进行merge
res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)
print(res)
# 将indicator的列改名
res = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_merge')


#index

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left)
print(right)
res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)
 
# solve overlapping problem
#如果两个dataframe有相同的列，则可以通过添加列的叙述来区分

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

print(boys)
print(girls)
res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
print(res)








