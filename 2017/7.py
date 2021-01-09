import fileinput
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])

D = defaultdict(list)
W = defaultdict(int)

for l in L:
	l = l.replace(',', ' ')
	l = l.split()
	if '->' in l:
		for i in range(3, len(l)):
			D[l[0]].append(l[i])
	W[l[0]] = int(l[1][1:-1])

for d1 in D:
	bottom_flag = True
	for d2 in D:
		if d1 != d2:
			if d1 in D[d2]:
				bottom_flag = False
				break
	if bottom_flag:
		bottom = d1
		break

print (bottom)

def calc_w(root):
	wa = W[root]
	for d in D[root]:
		wa += calc_w(d)
	return wa

# Create a graph with the total weight of a node
# and it child if it has
weight = defaultdict(int)
for d1 in D[bottom]:
	stack = [D[d1]]
	weight[d1] = calc_w(d1)
	while stack != []:
		group = stack.pop()
		for d2 in group:
			weight[d2] = calc_w(d2)
			stack.append(D[d2])

# Returns the child node that it is not balanced
# and the weight difference, returns '', 0 is there
# isn't any
def unbalanced_childs(root):

	if len(D[root]) == 0:
		return '', 0

	R = defaultdict(list)
	for d in D[root]:
		R[weight[d]].append(d)

	if len(R.keys()) == 1: # The subtree is balanced
		return '', 0

	# there is only with a different weight
	k = list(R.keys())
	if len(R[k[0]]) == 1:
		a,b = k[0],k[1]
	else:
		a,b = k[1],k[0]

	return R[a][0], a - b
	
root = bottom
while D[root] != []:
	uc, diff = unbalanced_childs(root)
	if uc != '':
		root = uc
		node = root
		weight_diff = diff
	else:
		break

print (W[node] - weight_diff)

# Sol input7.dat
#
# vmpywg
# 1674
#
# Time: 0.032 s
