import fileinput
from queue import PriorityQueue
from collections import defaultdict

L = [list(l.strip()) for l in fileinput.input()]
	
H = len(L)
W = len(L[0])

for i in range(H):
	for j in range(W):
		L[i][j] = int(L[i][j])

L2 = []
for m in range(5):
	for i in range(H):
		new_array = []
		for k in range(5):
			new_array += [l+k+m if (l+k+m) <= 9 else (l+k+m)%9  for l in L[i]]
		L2.append(new_array)

def dijkstra(L):
	H = len(L)
	W = len(L[0])
	INF = 1000000000
	risks = [[INF for j in range(W)] for i in range(H)]
	risks[0][0] = 0
	
	node = (0,0)
	visited = defaultdict(tuple)
	queue = PriorityQueue();
	queue.put((0,node))
	while not queue.empty():
		curr_risk, node = queue.get()
		visited[node] = True
	
		[x,y] = node
		for (i,j) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
			if 0<=i and 0<=j and i<H and j<W:
				if not visited[(i,j)]:
					if curr_risk + L[i][j] < risks[i][j]:
						risks[i][j] = curr_risk + L[i][j]
						queue.put((risks[i][j],(i,j)))
	return risks[H-1][W-1]

print(dijkstra(L))
print(dijkstra(L2))

# Sol input15.dat
#
# 456
# 2831
#
# Time: 1.29 s
