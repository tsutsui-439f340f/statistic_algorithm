import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
niter=5000
step=0.5
 
x=0
nac=0
u=[]
mean=[]
val=[]
s=[]
p=[]
for i in range(1,niter+1):
	back=x
	init=0.5*x*x
	dx=np.random.rand()
	dx=(dx-0.5)*step*2
	x=x+dx
	fin=0.5*x*x
	met=np.random.rand()
	if np.exp(init-fin)>met:
		nac=nac+1
	else:
		x=back
#	print(x,nac//i)
	u.append(x)
	mean.append(np.mean(u))
	s.append(x*x)
	p.append(np.exp(-(x*x)*0.5)/np.sqrt(2*np.pi))
	
	val.append(np.mean(s))


plt.plot(u,'-o',label='x',c='green',alpha=0.1)
plt.plot(mean,'--',c='blue',label='x_mean')
plt.plot(val,'red',label='x*x_mean')
#plt.bar(u,p,0.05)
plt.grid()
plt.ylabel('X')
plt.xlabel('N')
plt.legend(loc='best')
plt.title('mcmc_exp(-x*x/2)/sqrt(2*pi)')
plt.show() 



#plt.bar(c,c)
#plt.show()
