import numpy as np
import matplotlib.pyplot as plt


def RBF(x,y):
	th1=1
	th2=1
	distance=similar_distance(x,y)
	
	return th1*np.exp(-np.abs(distance)**2/th2)

def similar_distance(x,y):
	n=x.shape[0]
	m=y.shape[0]
	z=np.ones((n,m))*y
	z=x-z.T
	
	return z

def gaussian(x,y,xx):
	k1=RBF(x,xx)#k.T
	k=np.linalg.inv(RBF(x,x))
	k2=RBF(xx,xx)
	
	mean=k1.dot(k.dot(y))
	sigma=k2-(k1.dot(k.dot(k1.T)))
	
	return mean,sigma


def __main__():
	#使い方:x,y,xxを用意する->p(y/x,y,xx)を推定する。
	#データセットx,y
	#テストデータxx
	
	x=np.array([2,45,76,235,234,23])
	y=np.array([46,2,46,23,6,43])
	xx=np.linspace(0,100,1000)
	
	mean,sigma=gaussian(x,y,xx)
	plt.scatter(x,y,c='#ff77aa')
	plt.plot(xx,mean,'r')
	std = np.sqrt(sigma.diagonal())
	plt.fill_between(xx,mean-std,mean+std,alpha=0.9,color='skyblue')
	plt.show()


__main__()

