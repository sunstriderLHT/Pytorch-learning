import torch

cond = torch.tensor([[0.6769, 0.7271], [0.8884, 0.4163]])
print(cond)
a = torch.tensor([[0, 0], [0, 0]])
b = torch.tensor([[1, 1], [1, 1]])
# where 按照cond选择对应的矩阵的元素
# 高度调用Gpu 高度并行
print(torch.where(cond>0.5, a, b))
