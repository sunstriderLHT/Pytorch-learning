import numpy
import torch

a = torch.rand(4, 3, 28, 28)  # (batch_size,channel, height, width)

print(a[0].shape)

print(a[0, 0].shape)

print(a[0, 0, 2, 4])

print(a.shape)

print(a[:2].shape)  # 选取第一个维度的前两个元素0，1，不包含2

print(a[:2, :1, :, :].shape)  # :1 从0取到1，不包含1

print(a[:2, 1:, :, :].shape)  # 1: 一共有0，1，2三个通道，从1取到最后一共两个

print(a[:2, -1:, :, :].shape)  # -1: 从最后一个元素取到最后， 一共一个元素

# 隔行采样
print(a[:, :, 0:28:2, 0:28:2].shape)  # start:end:interval
print(a[:, :, ::2, ::2].shape)

# select by specific index
print(a.index_select(0, torch.tensor([0, 1])).shape)  # (对哪一维度操作, 用tensor表示选取这个维度的哪些元素)

print(a.index_select(1, torch.tensor([0, 2])).shape)

print(a.index_select(2, torch.arange(8)).shape)

# ... 自动补全维度
print(a[...].shape)
print(a[0, ...].shape)  # 也就是a[0]
print(a[0, ..., ::2].shape)  # 也就是a[0, :, :, ::2]

# select by mask

x = torch.randn(3,4)
print(x)

mask = x.ge(0.5) # x中greater or equal 0.5的元素记为True，其他记为False

print(mask)

print(mask.dtype)

print(torch.masked_select(x, mask))  # 从x中选取出大于等于0.5的元素

# select by flatten index

src = torch.tensor([[4, 3, 5],
                   [6, 7, 8]])

print(torch.take(src, torch.tensor([0, 2, 5])))  # 将tensor打平后选取

