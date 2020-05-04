import matplotlib.pyplot as plt
import numpy as np

#添加注释
x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',linewidth=2.5)   # k--代表 color ='black',linestyle='--' 
plt.plot([x0,0],[y0,y0],'k--',linewidth=2.5)

# method 1
# xy 为被注释的坐标点，xycoords 选择指定的坐标轴系统， xytext为注释文字的坐标位置 
# textcoords text的坐标轴系统，此处是以注释点为原心

plt.annotate(r'$2x+1=%s$' %y0,xy=(x0,y0),xycoords='data',xytext=(30,-30),
textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',
connectionstyle='arc3,rad=.2'))

# method 2 
plt.text(-3.7,3,r'$This\ is\ some\ text. \mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16,'color':'r'})


plt.show()

