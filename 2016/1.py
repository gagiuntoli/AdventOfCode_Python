import fileinput

L = list([l.strip() for l in fileinput.input()])

line = L[0]

line = line.split(', ')

P = []

hor = 0
ver = 0
d = 0

P.append((hor,ver))
found = False
hor_r = 0
ver_r = 0

for l in line:
	m = l[0]
	n = int(l[1:])
	if m == 'L':
		d = (d - 1) % 4
	else:
		d = (d + 1) % 4

	dh = 0
	dv = 0
	if d == 0:
		dh = n
	elif d == 1:
		dv = n
	elif d == 2:
		dh = -n
	else:
		dv = -n

	if not found:
		if dh != 0:
			step = 1 if dh > 0 else -1
			for i in range(hor + step, hor + dh + step, step):
				if (i, ver) in P:
					hor_r = i
					ver_r = ver
					found = True
				else:
					P.append((i,ver))
		else:
			step = 1 if dv > 0 else -1
			for i in range(ver + step, ver + dv + step, step):
				if (hor, i) in P:
					hor_r = hor
					ver_r = i
					found = True
				else:
					P.append((hor,i))

	hor += dh
	ver += dv
	
print (abs(hor + ver))
print (abs(hor_r + ver_r))
	
