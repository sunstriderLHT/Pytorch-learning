import torch
from torch.nn import functional as F

# 单输出感知机
x = torch.randn(1, 10)
w = torch.randn(1, 10, requires_grad=True)

o = torch.sigmoid(x@w.t())
print(o.shape)

loss = F.mse_loss(torch.ones(1,1), o)
print(loss.shape)

loss.backward()
print(w.grad)

# 多输出感知机
x = torch.randn(1, 10)
w = torch.randn(2, 10, requires_grad=True)

o = torch.sigmoid(x@w.t())
print(o.shape)

loss = F.mse_loss(torch.ones(1, 2), o)
print(loss)

loss.backward()

print(w.grad)