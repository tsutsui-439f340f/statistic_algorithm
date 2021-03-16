import numpy as np
import matplotlib.pyplot as plt


dx=0.01

x=np.arange(-8,8.1,0.1)
mu1=0
mu2=np.arange(-4,4.1,0.1)

sigma1=1
sigma2=1

mx=[]
js_point=[]

p=np.exp(-((x-mu1)**2)/2*(sigma1**2))/np.sqrt(2*np.pi*(sigma1**2))

fig,ax=plt.subplots(2,1,figsize=(12,6))

for m in mu2:
	q=np.exp(-((x-m)**2)/2*(sigma2**2))/np.sqrt(2*np.pi*(sigma2**2))
	js_div=np.sum(p*np.log(p/((p+q)/2))*dx)/2+np.sum(q*np.log(q/((p+q)/2))*dx)/2
	mx.append(js_div)

mu_point=np.arange(-4,4.1,2)
for m in mu_point:
	q=np.exp(-((x-m)**2)/2*(sigma2**2))/np.sqrt(2*np.pi*(sigma2**2))
	js_div=np.sum(p*np.log(p/((p+q)/2))*dx)/2+np.sum(q*np.log(q/((p+q)/2))*dx)/2
	js_point.append(js_div)
	ax[0].plot(x,q)

ax[0].plot(x,p)

ax[1].plot(mu2,mx)
ax[1].plot(mu_point,js_point,'*',markersize=10)
plt.show()

