import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    #label后面的background box,facecolor是box颜色，edgecolor是box边框颜色，alpha为不透明度，越低越透
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.9))   


plt.show()

#ax.get_xticklabels() 获取x轴的labels
#label.set_bbox() 设置label的background box 接收一个dictionary
