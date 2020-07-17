import torch
# match from last dim

# why broadcasting
# 1. for actual demanding
#   [class, students, scores]
#   add bias for every students: +5 score
#   [4, 32, 8] + [5.0]
#   [4, 32, 8] + [4, 32, 8]
# 2. memory consumption
#   [4, 32, 8] ==>  1024B
#   [5.0]      ==>  1B

# when it has no dim
# 如果没有这个维度就按照另一个tensor补全
# when it has dim of size 1
# 如果有这个维度且维度形状为1，则扩展到这个tensor的形状
# 如果有这个维度但是形状不为1，则无法使用broadcasting

x = torch.empty(1)
y = torch.empty(3, 1, 7)
print((x+y).size())
