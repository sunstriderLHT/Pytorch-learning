import torch
from torch.nn import functional as F
# sigmoid/logistic
# sigmoid()derivative = sigma*(1-sigma)
a = torch.linspace(-100, 100, 10)
print(a)
print(torch.sigmoid(a))  # 将矩阵元素转化为0-1的值

# Tanh(RNN)
# Tanh() derivative = 1-tanh(x)**2
a = torch.linspace(-1, 1, 10)
print(a)
print(torch.tanh(a))  # 将矩阵元素转化为-1到1的值

# ReLU Rectified Linear Unit
# when x<0 f(x)=0, when x>0, f(x)=x
#  x<0,derivative=0, x>0,derivative=1
a = torch.linspace(-1, 1, 10)
print(torch.relu(a))
print(F.relu(a))