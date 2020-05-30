import numpy as np
import matplotlib.pyplot as plt






X=np.linspace(-1,1,10)
data=X**2-X+np.random.randn(10)
#y=[np.sin(2*np.pi*2*x),x**2,-x-4,x**3-8*x**2,np.sinc(x)]


def ridge(x,b=1):
	kx=np.ones((x.shape[0],x.shape[0]))*x.reshape(-1,1)
	kx-=x
	
	return np.exp(-b*(kx)**2)

lamda=[0.1,0.3,0.5,1]
y=[]
n=2
m=2
k=ridge(X,b=1)
for l in lamda:
	a=np.linalg.inv(k+l*np.eye(X.shape[0]))*data
	y.append(np.sum(a*k,axis=1))
fig,ax=plt.subplots(n,m,figsize=(8,8))


c=0
for i in range(n):
	for j in range(m):
		ax[i,j].plot(X,y[c],'-o',c="red")
		ax[i,j].scatter(X,data)
		ax[i,j].set_title("lamda={}".format(lamda[c]))
		c+=1
		
		if c==4:
			break
		
		
plt.show()
