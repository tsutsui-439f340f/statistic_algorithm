import numpy as np

#viaの数字は前ノード番号で経由先が要素番号
#via=[-1,0,1] example: ノード1に行くにはノード0経由する必要がある、ノード2に行く必要がある

def d(s,goal):
	cost[s]=0
	via[s]="init"
	
	while True:
		min=10000
		c=0
		for x in range(n):
			#先にノード間の重みの小さい方を見つけたらそれ以上条件を満たすことはない
			#targetは最終的に選ばれたノードになる
			#ifは隣接ノード間の探索
			if used[x]!=1 and min>cost[x]:
				min=cost[x]
				target=x
				print("next x",x)
		print("target x",target)
		
		if target==goal:
			return cost[goal],via
		#disy[x][y]に入力されていなければcost[y]は条件を満たさないのでyを更新しない
		
		#target=0で1回目はcost[0]=0よりcost[1]=10000>隣接ノード重み+cost[0]だから更新され
		for y in range(n):
			if cost[y]>dist[target][y]+cost[target]:
				cost[y]=dist[target][y]+cost[target]
				via[y]=target
				c+=1
				print(y,cost[y])
				#print(via)
		if c==0:
			print("隣接ノードなし")	
		used[target]=1
		
		
		
		print("----------")


n=16

cost=np.ones(n)*10000

used=np.zeros(n)
#via=np.ones(n)*(-1)

via={}
for i in range(n):
	via[i]=-1

dist=np.ones((n,n))*10000

"""
s=int(input("start"))
g=int(input("goal"))

h=int(input("入力ノード数"))

for i in range(h):
	print("{}: ".format(i))
	a=int(input("前ノード"))
	b=int(input("後ノード"))
	l=int(input("重み"))
	dist[a][b]=l
"""

s=0
g=7

dist[0][1]=4
dist[0][2]=2
dist[2][3]=3
dist[2][4]=1
dist[4][5]=3
dist[4][3]=1
dist[3][6]=3
dist[5][7]=8
dist[5][6]=8
dist[7][8]=4

dist[8][9]=5
dist[9][10]=1
dist[3][7]=16

n,v=d(s,g)
print()
print("最終コスト{}".format(n))
print()
print("後ノード <- 前ノード:{}".format(v))






