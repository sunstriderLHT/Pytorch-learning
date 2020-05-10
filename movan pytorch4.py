# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:58:33 2020

@author: 16132
"""

#regression
import torch 
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

#fake data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # 把一维数据转二维数据
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

x, y  = Variable(x), Variable(y)

#plt.scatter(x.data.numpy(),y.data.numpy())
#plt.show()

class Net(torch.nn.Module):
    def __init__(self,n_features,n_hidden,n_output):
        #存储搭建网络的信息
        super(Net,self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden,n_output)
        pass
    
    def forward(self, x):
        #神经网络前向传递的过程，将信息组合
        x = F.relu(self.hidden(x)) #用激励函数嵌套隐藏层的信息
        x = self.predict(x)
        return x 

net = Net(1, 10, 1)
print(net)

plt.ion()  #实时打印
plt.show()

optimizer = torch.optim.SGD(net.parameters(), lr = 0.5)
loss_func = torch.nn.MSELoss() #均方差计算误差
for t in range(100):
    prediction = net(x)
    
    loss = loss_func(prediction,y)
    
    optimizer.zero_grad() #把梯度归零
    loss.backward() #反向传递
    optimizer.step() #以learning rate的速率优化
    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x.data.numpy(),y.data.numpy())
        plt.plot(x.data.numpy(),prediction.data.numpy(),'g-',lw = 2)  #(x,y,'color',lw=line width)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)
plt.ioff()
plt.show()












