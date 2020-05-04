# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:47:56 2020

@author: 16132
"""
import numpy as np
#分割array
A = np.arange(12).reshape(3,4)
print(A)

print(np.split(A, 2, axis=1)) #按列拆分
print(np.split(A, 3, axis=0)) #按行拆分
print(np.array_split(A, 3, axis=1)) #array_split 不等量分割

print(np.vsplit(A,3)) #上下拆分
print(np.hsplit(A,2)) #左右拆分