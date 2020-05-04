import matplotlib.pyplot as plt
import numpy as np

#移动坐标轴
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

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)   #用创建的列表中的元素替换x轴的坐标序列

plt.yticks([-2,-1.8,-1,1.22,3,],
        [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$']) #用文字label来代替原有的ticks
# gca ='get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')    # spine 是figure 的脊梁也就是图片的四个边框
ax.spines['top'].set_color('none') 
ax.xaxis.set_ticks_position('bottom')  # 用下脊梁代替x坐标轴
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))   #设置x轴位置为y=0的位置  
ax.spines['left'].set_position(('data',0))

plt.show()

#ax = plt.gca() 获取当前的坐标轴

#ax.spines[''].set_color('')  第一个括号中可以填right,left,top,bottom表示figure的四条边框线

#第二个括号填入颜色  none表示没有颜色

#ax.xaxis.set_ticks_position('')  选择用哪根spine来表示为x轴

#ax.spines[''].set_position(('data',0))  设定spine的位置  'data'表示在默认坐标系中

