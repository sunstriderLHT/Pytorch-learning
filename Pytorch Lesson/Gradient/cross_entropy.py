import torch
from torch.nn import functional as F

# entropy - measure of surprise
# 熵越高，惊喜越小

# KL divergence 两个函数越接近，KLD就越接近于0
x = torch.randn(1, 784)
w = torch.randn(10, 784)

logits = x@w.t()
print(logits.shape)
# 使用cross_entropy时默认对输入使用softmax+log, 第二个输入值指的是目标分类的序号
loss = F.cross_entropy(logits, torch.tensor([4]))
print(loss)
# 想要自己用softmax得话用下面的代码
pred = F.softmax(logits, dim=1)
pred_log = torch.log(pred)
print(pred_log)
loss2 = F.nll_loss(pred_log, torch.tensor([4]))
print(loss2)
