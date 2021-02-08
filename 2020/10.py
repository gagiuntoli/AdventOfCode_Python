import fileinput

def count13(L):
	c1 = 0
	c3 = 0
	for i in range(1, len(L)):
		diff = L[i] - L[i-1]
		if diff == 1:
			c1 += 1
		if diff == 3:
			c3 += 1
	return c1 * c3

def count(L):
	D = [0 for x in range(len(L))]
	D[0] = 1
	for i in range(1, len(L)):
		c = 0
		for j in range(0, i):
			if abs(L[j] - L[i]) <= 3:
				c += D[j]
		D[i] = c
	return D[len(L)-1]

L = [int(x) for x in list([l.strip() for l in fileinput.input()])]
L = [0] + L + [max(L) + 3]
L.sort()

print(count13(L))
print(count(L))

L = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
assert count13(L) == 35
assert count(L) == 8

# Sol input10.dat
#
# 1755
# 4049565169664
#
# Time: 0.015 s
