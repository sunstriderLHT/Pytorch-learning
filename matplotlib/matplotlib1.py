import matplotlib.pyplot as plt
import numpy as np

#创建窗口
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()     #后续代码均是在同一个figure中绘制图象
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')  #设定线段颜色，宽度和样式

plt.show()

#plt.figure(num=1,figsize=(8,5)) 创建一个figure开始画图,可以自定义figure名字和大小

#plt.plot(x,y，color='',linewidth=,linestyle='') 根据x,y开始绘制连续的线型图象 可以自定义颜色线宽和样式