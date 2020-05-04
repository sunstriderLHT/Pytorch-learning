# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:59:34 2020

@author: 16132
"""

import numpy as np

A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))  #打印最小值的索引
print(np.argmax(A))  #打印最小值的索引

print(np.mean(A,axis=1))  #矩阵的平均值 axis=1 对每行求平均，axis=0 对每列求平均
print(A.mean())

print(np.average(A))

print(np.median(A))  #矩阵的中位数

print(np.cumsum(A))  #矩阵元素累加获得的array

print(np.diff(A))   #每两个数的差 以行为单位

print(np.nonzero(A)) #返回矩阵中非零的行索引和列索引

print(np.sort(A))   #以行为单位排序

print(np.transpose(A))  #转置矩阵
print((A.T).dot(A))

print(np.clip(A,5,9))  #把矩阵中小于5的数变为5，大于9的数变为9