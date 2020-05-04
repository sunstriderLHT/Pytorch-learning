# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:12:48 2020

@author: 16132
"""
import numpy as np
#合并array
A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B)) #vertical stack上下合并
D = np.hstack((A,B)) #horizontal stack左右合并


print(A[np.newaxis,:].shape) #增加行数
print(A[:,np.newaxis].shape)  #增加列数

A = A[:,np.newaxis]
B = B[:,np.newaxis]
D = np.vstack((A,B))
print(D)

E = np.concatenate((A,B,B,A),axis=0) #行合并，axis=1列合并
print(E)
F = np.concatenate((A,B),axis=1)
print(F)