import fileinput

L = list([l.strip() for l in fileinput.input()])

a = [int(x) for x in L[0].split()]

P = {}
cy = 0
while True:
	m = max(a)
	i = 0
	while a[i] != m:
		i += 1
	c = a[i]
	a[i] = 0
	
	while c > 0:
		i += 1
		i %= len(a)
		a[i] += 1
		c -= 1

	if tuple(a) in P:
		size = cy - P[tuple(a)] 
		break	
	else:
		P[tuple(a)] = cy
	cy += 1

print (cy + 1)
print (size)

# Sol input6.dat
#
# 3156
# 1610
#
# Time: 0.028 s
