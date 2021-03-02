import numpy as np
import matplotlib.pyplot as plt


#カーネル関数
def K(x,x_dash,th1=1,th2=1,name='gauss'):
	distance=similar_distance(x,x_dash)
	
	if name=='gauss':
		return th1*np.exp(-np.abs(distance)**2/th2)
	elif name=='exp':
		return np.exp(-(np.abs(distance))/th1)
	elif name=='phase':
		return np.exp(th1*np.cos(np.abs(distance)/th2))

#データの距離のマップを計算する
def similar_distance(x,x_dash):
	n=x.shape[0]
	m=x_dash.shape[0]
	z=np.ones((n,m))*x_dash
	z=x-z.T	
	return z.T

#もとデータ
x=np.linspace(0,20,100)
y=2*np.sin(x)+3*np.cos(2*x)+5*np.sin(2/3*x)+np.random.randn(len(x))

#サンプリング数
n=30

sample_arg=np.random.randint(0,x.shape[0],n)
sample_arg=np.unique(sample_arg)

#サンプルデータ
x_train=x[sample_arg]

y_train=y[sample_arg]


x_pre=x

#パラメータ
th1=20
th2=0.5

#ガウス過程
def GP(x_train,y_train,x_pre,th1,th2):
	k=K(x_train,x_train,th1=th1,th2=th2)
	k_inv=np.linalg.inv(k)
	k_s=K(x_train,x_pre,th1=th1,th2=th2)
	k_ss=K(x_pre,x_pre,th1=th1,th2=th2)
	kk=np.dot(k_s.T,k_inv)
	
	mean=np.dot(kk,y_train)
	
	var=k_ss-k_s.T.dot(k_inv.dot(k_s))
	
	return mean,var


mean,var=GP(x_train,y_train,x_pre,th1,th2)
plt.plot(x,y,label="original")
plt.plot(x_train,y_train,'o',label="sample")

for _ in range(10):
	plt.plot(x_pre,np.random.multivariate_normal(mean,var),'--')


std= np.sqrt(np.abs(var.diagonal()))*2
plt.fill_between(x_pre,mean+std,mean-std,alpha=.2)
		
plt.legend(loc="best")
plt.grid()

plt.show()


