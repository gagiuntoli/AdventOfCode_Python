import fileinput

def memory(n):
	x = 0
	y = 0
	d = 1
	di = 0 # start in x+
	for i in range(1, n):
		if di == 0 and x < d:
			x += 1
		if di == 1 and y < d:
			y += 1
		if di == 2 and x > -d:
			x -= 1
		if di == 3 and y > -d:
			y -= 1
		if x == d:
			di = 1
		if y == d:
			di = 2
		if x == -d:
			di = 3
		if y == -d:
			di = 0
			d += 1
		#print (x, y)
	return abs(x) + abs(y)

def memory2(n):
	P = {}
	x = 0
	y = 0
	d = 1
	di = 0 # start in x+
	s = 1
	P[(x, y)] = s

	while s < n:
		if di == 0 and x < d:
			x += 1
		if di == 1 and y < d:
			y += 1
		if di == 2 and x > -d:
			x -= 1
		if di == 3 and y > -d:
			y -= 1
		if x == d:
			di = 1
		if y == d:
			di = 2
		if x == -d:
			di = 3
		if y == -d:
			di = 0
			d += 1
		s = 0
		if (x+1,y) in P:
			s += P[(x+1,y)]
		if (x+1,y+1) in P:
			s += P[(x+1,y+1)]
		if (x,y+1) in P:
			s += P[(x,y+1)]
		if (x-1,y+1) in P:
			s += P[(x-1,y+1)]
		if (x-1,y) in P:
			s += P[(x-1,y)]
		if (x-1,y-1) in P:
			s += P[(x-1,y-1)]
		if (x,y-1) in P:
			s += P[(x,y-1)]
		if (x+1,y-1) in P:
			s += P[(x+1,y-1)]
		#print (x,y,s)
		P[(x, y)] = s
	return s

L = list([l.strip() for l in fileinput.input()])

n = int(L[0])

print(memory(n))
print(memory2(n))

# Sol input3.dat
#
# 326
# 363010
#
# Time: 0.087 s
