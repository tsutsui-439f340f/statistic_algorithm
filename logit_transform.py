import numpy as np
#ロジット変換 p:確率
def logit(p):
	return np.log(p/(1-p))
#ロジット逆変換
def ilogit(p):
	return 1/(1+np.exp(-p))
#調整確率
def revise(x,n):
	return (x+0.5)/(n+1)
#確率
def rate(x,n):
	return x/n

x=199
n=12404

print(rate(x,n))
p=rate(x,n)
print(revise(x,n))

print(logit(p))
l=logit(p)
print(ilogit(l))
