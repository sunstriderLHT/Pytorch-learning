# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:18:14 2020

@author: 16132
"""

import torch
import numpy as np

np_data = np.arange(6).reshape((2,3))

#torch.from_numpy(): convert ndarray to tensor
torch_data = torch.from_numpy(np_data)

#torch_data.numpy(): convert tensor to ndarray
tensor2array = torch_data.numpy()

print(
    '\nnumpy array:\n', np_data,          # [[0 1 2], [3 4 5]]
    '\ntorch tensor:\n', torch_data,      #  0  1  2 \n 3  4  5    [torch.LongTensor of size 2x3]
    '\ntensor to array:\n', tensor2array, # [[0 1 2], [3 4 5]]
)

# matrix multiplication 矩阵点乘   
# np.matmul
# torch.mm
data = [[1,2],[3,4]]
tensor = torch.FloatTensor(data)# 转换为32位浮点tensor

print(
      '\nmatrix multiplication:',
      '\nnumpy:\n',np.matmul(data,data),
      '\ntorch:\n',torch.mm(tensor,tensor)
      )1

#tensor.dot()只能针对一维数组