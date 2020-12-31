import fileinput
import re

L = list([l.strip() for l in fileinput.input()])

P = {}
O = {}
count = 0

for l in L:
	reg = re.findall(r'\d+', l)
	idn = int(reg[0])
	x = int(reg[1])
	y = int(reg[2])
	dx = int(reg[3])
	dy = int(reg[4])
	O[idn] = 0
	for ix in range(x, x + dx):
		for iy in range(y, y + dy):
			if (ix, iy) in P:
				if P[(ix, iy)] != -1:
					count += 1
					O[P[(ix, iy)]] += 1
					P[(ix, iy)] = -1
				O[idn] += 1
			else:
				P[(ix, iy)] = idn

print (count)

for i in O:
	if O[i] == 0:
		idn_s = i
print(idn_s)
			
# Sol input3.dat
#
# 118858
# 1100
#
# Time: 0.239 s
