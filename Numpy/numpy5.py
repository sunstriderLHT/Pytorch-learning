# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:55:46 2020

@author: 16132
"""

import numpy as np
A = np.arange(3,15).reshape((3,4))
print(A)

print(A[2])
print(A[2,:])

print(A[1][1])
print(A[1,1])

for row in A:   #默认迭代每一行
    print(row)

for column in A.T: #通过转置矩阵实现迭代每一列
    print(column)

print(A.flatten())  #把矩阵输出为一个array

for item in A.flat:  #A.flat得到一个迭代器里面是一个array
    print(item)