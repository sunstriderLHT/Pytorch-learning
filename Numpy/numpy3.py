# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:41:33 2020

@author: 16132
"""

import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(b<3,'\n') #return True if element fulfill the condition

print(a,b,'\n')
c = a-b
print(c,'\n')

d = 10*np.tan(a)
print(d,'\n')

e = np.array([[1,1],
              [0,1]])
f = np.arange(4).reshape((2,2))
print(e,'\n')
print(f,'\n')

g = e*f  #simple multify
print(g,'\n')

g_dot = np.dot(e,f) #dot multify
print(g_dot,'\n') 
g_dot_2 = e.dot(f)
print(g_dot_2,'\n')

h = np.random.random((2,4))
print(h)

print(np.sum(h,axis=1)) #axis = 1, count sum in the row; axis = 0, count sum in the column
print(np.min(h))
print(np.max(h))