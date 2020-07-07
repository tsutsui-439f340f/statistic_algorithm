import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from mpl_toolkits.mplot3d import axes3d
from matplotlib import  cm

niter=6000
#step 1以上で平均に収束
step_x=0.09
step_y=0.03
x=0
y=0

f=0

nac=0
u_x=[]
mean_x=[]
val_x=[]
s_x=[]
p=[]

u_y=[]
mean_y=[]
val_y=[]
s_y=[]
s_xy=[]
for i in range(1,niter+1):
	back_x=x
	back_y=y
	init=0.5*(x*x+y*y+x*y)
	
	dx=np.random.rand()
	dx=(dx-0.5)*step_x*2
	
	dy=np.random.rand()
	dy=(dy-0.5)*step_y*2
	x=x+dx
	y=y+dy
	fin=0.5*(x*x+y*y+x*y)
	met=np.random.rand()
	if np.exp(init-fin)>met:
		nac=nac+1
	else:
		x=back_x
		y=back_y
#	print(x,nac//i)
	u_x.append(x)
	mean_x.append(np.mean(u_x))
	u_y.append(y)
	mean_y.append(np.mean(u_y))
	s_y.append(y*y)
	s_xy.append(x*y)
	p.append(np.exp(-(x*x+y*y+x*y)/2)/np.sqrt(2*np.pi))
	
	#val.append(np.mean(s))


#plt.plot(u)
#plt.plot(mean,'--',c='blue')
#plt.plot(val,'red')
#plt.bar(u,p,0.05)

#x,yの分布
#plt.plot(u_x,u_y,'*')


plt.plot(mean_x,'--',label="x")
plt.plot(mean_y,'--',label='y')


"""
X,Y=np.meshgrid(np.linspace(-4,4,100),np.linspace(-4,4,100))
fig=plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(X, Y, p, rstride=2, cstride=5, cmap="hot")
"""
plt.grid()
plt.show() 



#plt.bar(c,c)
#plt.show()
