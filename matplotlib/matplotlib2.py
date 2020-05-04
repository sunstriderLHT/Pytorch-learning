import matplotlib.pyplot as plt
import numpy as np

#修改坐标轴
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-1,2))  #设置x的取值范围
plt.ylim((-2,3))
plt.xlabel('I am x')    #描述x轴
plt.ylabel('I am y')

new_ticks = np.linspace(-1,4,5)
print(new_ticks)
plt.xticks(new_ticks)   #用创建的列表中的元素替换x轴的坐标序列

plt.yticks([-2,-1.8,-1,1.22,3,4.5],
        [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$',r'$excellent$']) #用文字label来代替原有的ticks
plt.show()

#plt.xlim((-1,2))  #划定figure中x的取值
#plt.xticks(list)   #用list中的数字在x轴中贴label
#plt.yticks([ticks],[labels])   #用labels来替代ticks贴在y轴上