import numpy as np
import torch

# import from numpy
Q = np.array([2, 3.3])

torch.from_numpy(Q)

print(Q.dtype)

a = torch.tensor([2.2, 3])
b = torch.FloatTensor(2, 3)
c = torch.Tensor(2, 3)
# torch.tensor([]) 直接给数据
# torch.FloatTensor() 和 torch.Tensor() 括号里给tensor的shape
print(a)
print(b)
print(c)

print("************************************")

# 随机初始化

# rand 接受tensor的shape。并随机初始化，元素大小在[0，1]之间
d = torch.rand(3, 3)
print(d)

# rand_like 接受tensor，按照这个tensor的shape随机初始化一个tensor
print(torch.rand_like(d))

# randint(min,max,[shape]) 随机初始化一个元素大小介于[min,max)大小为shape的tensor
print(torch.randint(1, 10, [3, 3]))

# randn 均值为0方差为1
e = torch.randn(3, 3)
print(e)

# 用一个值填充整个tensor
f = torch.full([2, 3], 7)
print(f)

# 输出一个scalar
g = torch.full([], 7)
print(g)

# 输出一个一维tensor
h = torch.full([1], 7)
print(h)

# arange/ range
# arange(10) 生成一个1-10不含10的等差数列
print(torch.arange(10))

print(torch.arange(0, 10, 2))

print(torch.range(0, 10))  # 生成0-10等差数列包含10

# linspace/logspace

# linspace 指定区间 等距离切分
print(torch.linspace(0, 10, steps=4))

# logspace 10的多少次方
print(torch.logspace(0, 2, steps=10))

# ones/zeros/eye
torch.ones(3, 3)

torch.zeros(3, 3)

# eye 只能接收2维
print(torch.eye(3))

print(torch.eye(3,4))

# randperm 随机打乱
print(torch.randperm(10))
