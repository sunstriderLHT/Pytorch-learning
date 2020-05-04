# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:06:48 2020

@author: 16132
"""

import numpy as np

a = np.arange(4)
print(a)
b = a 
c = a 
d = b

print(b is a) #b就是a, 改变a就会改变b
a[0] = 11
print(a)
print(b)

print(d is a)

b = a.copy() #deep copy把a的值赋给b但不关联
a[3] = 44
print(a)
print(b)
