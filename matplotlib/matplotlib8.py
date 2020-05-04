import matplotlib.pyplot as plt
import numpy as np
# 柱状图
n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,Y1,facecolor='#9999ff',edgecolor='black')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    # ha: horizontal alignment横向对齐方式居中
    # va: vertical alignment 竖向对齐方式向下
    plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')

for x,y in zip(X,Y2):
    
    plt.text(x,-y-0.05,'-%.2f'%y,ha='center',va='top')
plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()

# zip()将可迭代对象中对应元素打包成一个个元组 返回由这些元组组成的列表

