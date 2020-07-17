import torch

# view/reshape

a = torch.rand(4, 1, 28, 28)

print(a.shape)

print(a.reshape(4, 28 * 28))  # 将原tensor转换为[4,784]的tensor

print(a.view(4, 28 * 28).shape)

# squeeze/ unsqueeze
# unsqueeze 取值范围是[-a.dim()-1,a.dim()+1) 此处是[-5,4) 正数在序号前插，负数后插

print(a.unsqueeze(0).shape)  # 在0索引前插入一个维度

print(a.unsqueeze(-1).shape)  # 在最后一维后插入一个维度

# 让两个不同维度的变量相加
b = torch.rand(32)
f = torch.rand(4, 32, 14, 14)
b = b.unsqueeze(1).unsqueeze(2).unsqueeze(0)
print(b.shape)

# squeeze 维度删减，不给定参数，则挤压所有shape为1的维度
print(b.squeeze(0).shape)  # 删减0维度
print(b.squeeze(-1).shape)  # 删除最后一个维度
print(b.squeeze(1).shape)  # 若当前维度的shape不为1，那么不进行删减

# expand/repeat 改变维度的shape
# expand: broadcasting 推荐 节约内存
a = torch.rand(4, 32, 14, 14)
print(b.shape)

# expand 前后的dimension必须一致
# 且只能改变shape为1的维度
print(b.expand(4, 32, 14, 14).shape)
# 若设定维度shape为-1则表示不改变这个维度的shape
print(b.expand(-1, 32, 4, -1).shape)

# repeat: memory copied 填入参数为复制原维度的次数
print(b.repeat(4, 32, 1, 1).shape)  # 会得到torch.Size([1*4,32*32,1*1,1*1])

print(b.repeat(4, 1, 14, 14).shape)

# transpose
a = torch.randn(3, 4)
print(a.t())  # .t()只能用于2维的transpose

# transpose()
a = torch.rand(4, 3, 32, 32)
# view原矩阵变换到其他大小，需要原矩阵tensor的内存是整块的
# a1 = a.transpose(1, 3).view(4, 3*32*32).view(4, 3, 32, 32)
# 这句话是无法执行的因为transpose后的a内存不是连续分布的

# 这句话没有按transpose后的维度展开，view造成了数据污染
a1 = a.transpose(1, 3).contiguous().view(4, 3 * 32 * 32).view(4, 3, 32, 32)
# [B, C, H, W]----->[B, W, H, C]---->[B, W*H*C]----->[B, C, W, H]
a2 = a.transpose(1, 3).contiguous().view(4, 3 * 32 * 32).view(4, 32, 32, 3).transpose(1, 3)
# [B, C, H, W]----->[B, W, H, C]---->[B, W*H*C]----->[B, W, H ,C]------->[B, C, H, W]
# 下面验证a1和a2是否与a完全一致
# 没有按transpose后的维度进行view操作，造成a1数据并不能和a对应上
print(torch.all(torch.eq(a, a1)))

print(torch.all(torch.eq(a, a2)))

# permute
# transpose只能一次进行两个维度的顺序交换
b = torch.rand(4, 3, 28, 32)  # 想要得到(4,28,32,3)
# 如果用transpose
print(b.transpose(1, 3).transpose(1, 2).shape)
# 如果用permute 实际上就是自动调用多次transpose操作来实现目的 所以还是会打乱内存顺序
print(b.permute(0, 2, 3, 1).shape)  # (0,1,2,3)---->(0,2,3,1)
