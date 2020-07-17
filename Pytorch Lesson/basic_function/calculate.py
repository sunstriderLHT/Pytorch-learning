import torch

a = torch.rand(3, 4)
b = torch.rand(4)

# basic + - * /
print(a+b)
print(torch.add(a, b))

print(torch.all(torch.eq(a-b, torch.sub(a, b))))

print(torch.all(torch.eq(a*b, torch.mul(a, b))))

print(torch.all(torch.eq(a/b, torch.div(a, b))))

# matrix multiply
# torch.mm(a,b) 只适用于2d
a = 3*torch.ones(2, 2)
b = torch.ones(2, 2)

print(torch.mm(a, b))
# matmul 和 @ 效果是一样的，都可对2d及以上matrix使用
print(torch.matmul(a, b))
print(a@b)

# 实例：降维过程
a = torch.rand(4, 784)
x = torch.rand(4, 784)
# pytorch 默认第一个参数为out(降维后维数)，第二个为in(降维前的维数)
w = torch.rand(512, 784)

print((x@w.t()).shape)

# 2d以上矩阵乘法
a = torch.rand(4, 3, 28, 64)
b = torch.rand(4, 3, 64, 32)
# 只对最后两维进行运算 前面保持不变
print(torch.matmul(a, b).shape)

b = torch.rand(4, 1, 64, 32)
print(torch.matmul(a, b).shape)

# power
a = torch.full([2, 2], 3.)  # 用3填满2*2的矩阵
print(a.pow(2))
print(a**2)

aa = a**2
print(aa.sqrt())
# 平方根的倒数
print(aa.rsqrt())

print(aa**0.5)

# exp  log
# exp 以e为底的指数函数
a = torch.exp(torch.ones(2, 2))
print(a)
# log 默认以e为底，要以2为底用log2(),以10为底用log10
print(torch.log(a))

# approximation
# .floor();.ceil();
a = torch.tensor(3.14)
# .floor() 向下取整
print(a.floor())
# .ceil()向上取整
print(a.ceil())
# .trunc()裁剪后的整数部分
print(a.trunc())
# .frac()裁剪后的小数部分
print(a.frac())
# .round()四舍五入
print(a.round())

# clamp
grad = torch.rand(2, 3)*15
print(grad.max())
print(grad.median())

# clamp(10) 把矩阵中小于10的元素改写为10
print(grad.clamp(10))
print(grad)
# clamp(5,10) 把矩阵中的元素限定在0到10之间，大于10的记为10,小于5的记作5
print(grad.clamp(5, 10))