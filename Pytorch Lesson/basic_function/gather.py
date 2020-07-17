import torch

prob = torch.randn(4, 10)
idx = prob.topk(dim=1, k=3)
idx = idx[1]
print(idx)
label = torch.arange(10) + 100
# 使用gather通过GPU高效将数据映射
print(torch.gather(label.expand(4, 10), dim=1, index=idx.long()))
