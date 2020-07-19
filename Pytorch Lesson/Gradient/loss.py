import torch
from torch.nn import functional as F

#  MSE mean squared error
# loss = sum((y-y')**2)
# 如果用L2-norm则要记得平方后才和loss函数相等
# torch.norm(y-y',2).pow(2)
x = torch.ones(1)
w = torch.full([1], 2.)
print(x, w)

# 想要对某个变量求导需要在之前进行说明，说明这个变量需要梯度信息
w.requires_grad_()
# 或 w = torch.tensor([1.],requires_grad=True)

# 写出mse函数，括号里填predict值和label值
mse = F.mse_loss(x * w, torch.ones(1))

# 进行自动求导，括号里第一个是函数，第二个是变量
gradient = torch.autograd.grad(mse, [w])
print(gradient)

# loss.backward
# 给函数中所有需要的梯度信息的变量附上梯度信息
# 通过.grad调用
mse = F.mse_loss(x * w, torch.ones(1))
mse.backward()
print(w.grad)

# 1.torch.autograd.grad(loss,[w1,w2]
# 2.loss.backward()
# 不管哪种方法都需要提前声明变量需要梯度信息
