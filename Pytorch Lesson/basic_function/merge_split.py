import torch

# cat stack
# cat
a = torch.rand(4, 32, 8)
b = torch.rand(5, 32, 8)
print(torch.cat([a, b], dim=0).shape)

# [class1-4, students, scores]
a1 = torch.rand(4, 3, 32, 32)
# [class5-9, students, scores]
a2 = torch.rand(5, 3, 32, 32)
print(torch.cat([a1, a2], dim=0).shape)

a2 = torch.rand(4, 1, 32, 32)
# print(torch.cat([a1, a2], dim=0).shape)
# Sizes of tensors must match except in dimension 0

print(torch.cat([a1, a2], dim=1).shape)

a1 = torch.rand(4, 3, 16, 32)
a2 = torch.rand(4, 3, 16, 32)
print(torch.cat([a1, a2], dim=2).shape)

# stack
print(torch.stack([a1, a2], dim=2).shape)
# 新增加一个维度，后面的维度形状保持不变, 所以合并前两个tensor形状必须完全一致
a = torch.rand(32, 8)
b = torch.rand(32, 8)
print(torch.stack([a, b], dim=0).shape)

# split chunk

# split
b = torch.rand(32, 8)
c = torch.stack([a, b, b], dim=0)

# 在第一个维度拆分c,每个子集形状为1
aa, bb, cc = c.split(1, dim=0)
print(aa.shape)
print(bb.shape)
aa, bb = c.split([2, 1], dim=0)
print(aa.shape)
print(bb.shape)

# chunk 按照数量拆分，下例拆为3份
aa, bb, cc = c.chunk(3,dim=0)
print(aa.shape)
print(bb.shape)