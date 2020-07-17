import torch

a = torch.randn(2, 3)

print(a.type())

print(type(a))

print(isinstance(a, torch.FloatTensor))

print("***************************************************")

# dimension = 0(scalar) , the final cost is this kind of data
b = torch.tensor(2.2)

print(b.shape)  # return torch.Size([]) means b is a scalar

print(len(b.shape))  # return the dimension of the data

print(b.size())  # same with .shape

print("***************************************************")

# dimension = 1, the bias and the linear input are this kind of data
c = torch.tensor([1.1])
print(c)
print("The shape of c is:{}".format(c.shape))

d = torch.tensor([1.1, 2.2])
print(d)
print("The shape of c is:{}".format(d.shape))  # dimension = 1, size = 2

print(torch.FloatTensor(2))  # randomly initiate

print("***************************************************")

# dimension = 2, linear input batch
e = torch.randn(2,3)

print(e, "\n", e.size())

print("The number of row is {0}, column is {1}".format(e.size(0), e.size(1)))

print("***************************************************")

# dim = 3, RNN Input Batch
f = torch.rand(1,2,3)

print(f)

print(f.shape)

# dim = 4, CNN

g = torch.rand(2,3,28,28)
print("The dimension of g is:{}".format(g.dim()))
print(g.shape)

print("2*3*28*28={0}".format(g.numel()))  # number of element(how many element inside the matrix)
