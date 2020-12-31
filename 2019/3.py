import fileinput

L = list([l.strip() for l in fileinput.input()])

l1 = L[0]
l2 = L[1]

l1 = l1.split(',')
l2 = l2.split(',')

P = {}
x = 0
y = 0

for i in l1:
	d = int(i[1:])
	if i[0] == 'R':
		for xi in range(x, x + d + 1):
			P[(xi, y)] = True
		x += d
	elif i[0] == 'L':
		for xi in range(x, x - d - 1, -1):
			P[(xi, y)] = True
		x -= d
	elif i[0] == 'U':
		for yi in range(y, y + d + 1):
			P[(x, yi)] = True
		y += d
	elif i[0] == 'D':
		for yi in range(y, y - d - 1, -1):
			P[(x, yi)] = True
		y -= d

I = {}
x = 0
y = 0
min_d = 10000000

for i in l2:
	d = int(i[1:])
	if i[0] == 'R':
		for xi in range(x, x + d + 1):
			if (xi, y) != (0,0) and (xi, y) in P:
				di = abs(xi) + abs(y)
				I[(xi, y)] = True
				if di < min_d:
					min_d = di
		x += d
	elif i[0] == 'L':
		for xi in range(x, x - d - 1, -1):
			if (xi, y) != (0,0) and (xi, y) in P:
				di = abs(xi) + abs(y)
				I[(xi, y)] = True
				if di < min_d:
					min_d = di
		x -= d
	elif i[0] == 'U':
		for yi in range(y, y + d + 1):
			if (x, yi) != (0,0) and (x, yi) in P:
				di = abs(x) + abs(yi)
				I[(x, yi)] = True
				if di < min_d:
					min_d = di
		y += d
	elif i[0] == 'D':
		for yi in range(y, y - d - 1, -1):
			if (x, yi) != (0,0) and (x, yi) in P:
				di = abs(x) + abs(yi)
				I[(x, yi)] = True
				if di < min_d:
					min_d = di
		y -= d

print (min_d)

D1 = {}
x = 0
y = 0
per = 0

for i in l1:
	d = int(i[1:])
	if i[0] == 'R':
		for xi in range(x, x + d + 1):
			if (xi, y) in I:
				D1[(xi, y)] = per
			per += 1
		per -= 1
		x += d
	elif i[0] == 'L':
		for xi in range(x, x - d - 1, -1):
			if (xi, y) in I:
				D1[(xi, y)] = per
			per += 1
		per -= 1
		x -= d
	elif i[0] == 'U':
		for yi in range(y, y + d + 1):
			if (x, yi) in I:
				D1[(x, yi)] = per
			per += 1
		per -= 1
		y += d
	elif i[0] == 'D':
		for yi in range(y, y - d - 1, -1):
			if (x, yi) in I:
				D1[(x, yi)] = per
			per += 1
		per -= 1
		y -= d

D2 = {}
x = 0
y = 0
per = 0

for i in l2:
	d = int(i[1:])
	if i[0] == 'R':
		for xi in range(x, x + d + 1):
			if (xi, y) in I:
				D2[(xi, y)] = per
			per += 1
		per -= 1
		x += d
	elif i[0] == 'L':
		for xi in range(x, x - d - 1, -1):
			if (xi, y) in I:
				D2[(xi, y)] = per
			per += 1
		per -= 1
		x -= d
	elif i[0] == 'U':
		for yi in range(y, y + d + 1):
			if (x, yi) in I:
				D2[(x, yi)] = per
			per += 1
		per -= 1
		y += d
	elif i[0] == 'D':
		for yi in range(y, y - d - 1, -1):
			if (x, yi) in I:
				D2[(x, yi)] = per
			per += 1
		per -= 1
		y -= d

min_d = 10000000
for (x, y) in D1:
	if D1[(x,y)] + D2[(x,y)] < min_d:
		min_d = D1[(x,y)] + D2[(x,y)]

print (min_d)


# Sol input3.dat
#
# 1674
# 14012
#
# Time: 0.117 s
