import torch

print(torch.__version__)
print('gpu:', torch.cuda.is_available())

z2 =list(range(3,31,3))
print(z2)