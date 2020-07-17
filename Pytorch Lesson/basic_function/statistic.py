import torch
a = torch.full([8], 1.)
b = a.view(2, 4)
c = a.view(2, 2, 2)
print(a)
print(b)
print(c)
# 求1-范数 元素绝对值之和
print(a.norm(1), b.norm(1), c.norm(1))
# 求2-范数 元素平方和开根号
print(a.norm(2), b.norm(2), c.norm(2))

# 给定dim 则给定维度消掉
# 下例中b维度为[2,4] 消掉dim=1,则得到结果shape为[2]
print(b.norm(1, dim=0))
print(b.norm(2, dim=0))
# c维度为[2，2，2] 消掉dim=0,则得到结果shape应为[2,2]
print(c.norm(1, dim=0))

# 统计属性
a = torch.arange(8).view(2, 4).float()
print(a)
# prod()累乘
print(a.min(), a.max(), a.mean(), a.prod())

print(a.sum())

# argmax以及argmin操作默认会将矩阵打平成一维向量然后标定序号
print(a.argmax(), a.argmin())

# 如果给定维度，则会在指定维度找到最大最小值
a = torch.randn(4, 10)
print(a[0])
print(a.argmax())
print(a.argmax(dim=1))

# dim keepdim
print(a)
# max会返回最大值以及最大值的下标
print(a.max(dim=1))
print(a.max(dim=1, keepdim=True))
print(a.argmax(dim=1, keepdim=True))

# topk 返回最大的几个元素以及下标
print(a.topk(3, dim=1))

# topk求最小的几个元素 将 largest设置为False
print(a.topk(3, dim=1, largest=False))

# kthvalue 求第8小的元素值和下标,默认在dim=1情况下进行运算
print(a.kthvalue(8))
print(a.kthvalue(3))
print(a.kthvalue(3, dim=0))

# compare
print(a>0)
# torch.gt a great大于 0
print(torch.gt(a, 0))

# torch.eq(a,b) 比较每个位置元素是否相等
a = torch.ones(2, 3)
b = torch.randn(2, 3)
print(torch.eq(a, b))
print(torch.eq(a, a))