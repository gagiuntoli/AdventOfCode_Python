import fileinput

L = list([l.strip() for l in fileinput.input()])

maxx = -1
maxy = -1
minx = 100000
miny = 100000
for i, c in enumerate(L):
	c = [int(x) for x in c.split(',')]
	L[i] = c
	if c[0] > maxx:
		maxx = c[0]
	if c[0] < minx:
		minx = c[0]
	if c[1] > maxy:
		maxy = c[1]
	if c[1] < miny:
		miny = c[1]

dx = maxx - minx + 1
dy = maxy - miny + 1

for i, l in enumerate(L):
	l[0] -= minx
	l[1] -= miny
	L[i] = l

def calc(L, inc):
	D = {}
	for x in range(0 - inc, dx + inc):
		for y in range(0 - inc, dy + inc):
			mind = 1000000
			for i, c in enumerate(L):
				d = abs(x - c[0]) + abs(y - c[1])
				if d < mind:
					mind = d
					minp = i
			dup = 0
			for c in L:
				d = abs(x - c[0]) + abs(y - c[1])
				if d == mind:
					dup += 1
			if dup == 1:
				if not minp in D:
					D[minp] = 1
				else:
					D[minp] += 1
	return D

D1 = calc(L, 0)
D2 = calc(L, 10)

maxc = -1000
for d in D1:
	if D1[d] == D2[d] and D1[d] > maxc:
		maxc = D1[d]
	
print(maxc)

inc = 0 # With 0 seems that the region is inside the box
count = 0
for x in range(0 - inc, dx + inc):
		for y in range(0 - inc, dy + inc):
			d = 0
			for c in L:
				d += abs(x - c[0]) + abs(y - c[1])
			if d < 10000:
				count += 1
print (count)
	
# Sol input6.dat
#
# 3989
# 49715
#
# Time: 3.719 s
