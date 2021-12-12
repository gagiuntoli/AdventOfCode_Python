import fileinput
from collections import defaultdict

L = [l.strip().split("-") for l in fileinput.input()]

G = defaultdict(list)
for line in L:
	G[line[0]].append(line[1])
	G[line[1]].append(line[0])

def isLower(string):
	return all(c.islower() for c in string)

def find_ways(G, node, visited, part):

	if node == "end":
		return 1
	elif node == "start" and visited[node] == 1:
		return 0
	elif part == 1 and visited[node] == 1:
		return 0
	elif part == 2 and list(visited.values()).count(2) > 0 and visited[node] >= 1:
		return 0
	else:
		if isLower(node):
			visited[node] += 1

	ways = 0
	for p in G[node]:
		ways += find_ways(G, p, visited.copy(), part)
	return ways

print(find_ways(G, "start", defaultdict(int),1))
print(find_ways(G, "start", defaultdict(int),2))


# Sol input12.dat
#
# 3679
# 107395
#
# Time: 0.71 s
