import torch
from torch.nn import functional as F
# softmax 满足每个返回值在0到1之间，所有返回值之和为1
# 输出节点对同序号的输入节点的导数为正
# 对不同序号的输入节点的导数为负
a = torch.rand(3)
a.requires_grad_()
print(a)

p = F.softmax(a, dim=0)
gradient1 = torch.autograd.grad(p[1], [a], retain_graph=True)
print(gradient1)
gradient0 = torch.autograd.grad(p[0],[a], retain_graph=True)
print(gradient0)
gradient2 = torch.autograd.grad(p[2], [a], retain_graph=True )
print(gradient2)