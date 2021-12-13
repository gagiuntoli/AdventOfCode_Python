import fileinput

L = [l.strip() for l in fileinput.input()]

F = []
D = {}
for line in L:
	if "," in line:
		[x, y] = line.split(",")
		D[(int(x),int(y))] = True
	if "fold" in line:
		line = line.split(" ")
		F.append([line[2][0], int(line[2][2:])])

X = max(d[0] for d in D)
Y = max(d[1] for d in D)

for i, fold in enumerate(F):
	
	points = list(D.keys()).copy()
	if fold[0] == "x":
		for (x,y) in points:
			if x > X//2 and x <= X:
				D[(X-x + (-1 if X % 2 == 1 else 0),y)] = True
		X //= 2
	else:
		for (x,y) in points:
			if y > Y//2 and y <= Y:
				D[(x,Y-y + (-1 if Y % 2 == 1 else 0))] = True
		Y //= 2

	if i == 0:
		num_points = sum((x <= X and y <= Y) for (x,y) in D)

print(num_points)
for y in range(Y):
	string = ""
	for x in range(X):
		if (x,y) in D:
			string += "#"
		else:
			string += "."
	print(string)

# Sol input13.dat
#
# 745
# ABKJFBGC
#
# Time: 0.02 s
