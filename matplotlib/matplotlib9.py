import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1-x/2+x**5+y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# 把x,y绑定为网格的输入值
X,Y = np.meshgrid(x,y) 

# plt.contourf 填充颜色到网格
plt.contourf(X,Y,f(X,Y),10,alpha=0.75,cmap=plt.cm.hot)
# 8 代表等高线分层数量
# plt.contour 等高线
C = plt.contour(X,Y,f(X,Y),10,colors='black',linewidth=.5)

# 添加标签
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()

# np.exp() 返回e的幂次方
# X,Y = np.meshgrid(x,y)  生成网格点坐标矩阵 
# 输入的x,y就是网格点的横纵坐标列向量
# 输出的X,Y就是坐标矩阵

# plt.contourf(x,y,z,part) 填充等高线f:filled
# plt.contour 绘制等高线

