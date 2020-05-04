import matplotlib.pyplot as plt
import numpy as np

#scatter 图

n=1024
#.random.normal(平均数，方差，数量)
X = np.random.normal(0,1,n) 
Y = np.random.normal(0,1,n)
# color value
T = np.arctan2(2*X,Y)


plt.scatter(X,Y,s=75,c=T,alpha=0.5)



plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
#隐藏ticks
plt.xticks(())
plt.yticks(())
plt.show()