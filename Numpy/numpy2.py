# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:57:51 2020

@author: 16132
"""

import numpy as np

a = np.array([[2,2,3],
              [2,3,4]],dtype=np.float)

b = np.zeros((3,4)) #create a matrix using 0
print(b)
c = np.ones((3,4)) #create a matrix using 1
print(c)
d = np.empty((3,4))  #create a matrix with no init
print(d)

e = np.arange(10,20,2)  #similar with range
print(e)

f = np.arange(12).reshape((3,4))   #reshape 里面要用括号括起来
print(f)

g = np.linspace(1,10,20).reshape((4,5))  #create 20 lines ranging from 1 to 10
print(g)