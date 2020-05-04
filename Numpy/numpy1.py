# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:51:43 2020

@author: 16132
"""
#创建array 以及array的一些属性
import numpy as np
array = np.array([[1,2,3],
                  [2,3,4]])
print(array)
print('number of dim:',array.ndim) #the number of dimesion of this array
print('shape:', array.shape) #the shape of this array (row,column)
print('size:',array.size) #the number of element in this array