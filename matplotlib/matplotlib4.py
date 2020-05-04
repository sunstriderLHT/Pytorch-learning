import matplotlib.pyplot as plt
import numpy as np

#创建图例
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()


plt.xlim((-1,2))  #设置x的取值范围
plt.ylim((-2,3))
plt.xlabel('I am x')    #描述x轴
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)   #用创建的列表中的元素替换x轴的坐标序列

plt.yticks([-2,-1.8,-1,1.22,3,],
        [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$']) #用文字label来代替原有的ticks


l1, = plt.plot(x,y2,label='up') #注意如果想要放到legend的handle中，要在l1后加个逗号
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
#在绘制图象时设置label  调用legend函数后就会在figure中生成图例
plt.legend(handles=[l1,l2], labels=['aaa','bbb'], loc='best')     # handles传入线段


plt.show()

#plt.legend(handles=[],labels=[],loc='')  
#handles中存放想要生成图例的图线，labels中放对应图线的标签，loc图例位置设置
