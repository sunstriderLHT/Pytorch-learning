# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:43:44 2020

@author: 16132
"""

import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, requires_grad = True)

print(tensor)
print(variable)

t_out = torch.mean(tensor*tensor) # x^2
v_out = torch.mean(variable*variable) 

print(t_out)
print(v_out)

v_out.backward() #误差反向传递
#v_out = 1/4*sum(var*var)
# d(v_out)/d(var) = variable/2
print(variable.grad)  
#v_out 和variable存在联系，
#误差反向传递会对variable的gradient 产生影响
print(variable.data)
print(variable.data.numpy())
#tensor 和 variable不一样，tensor可以和ndarray相互转换
#variable.data会得到tensor
#相当于说variable比tensor多了个requires_grad的属性
#tensor是variable中的数据部分