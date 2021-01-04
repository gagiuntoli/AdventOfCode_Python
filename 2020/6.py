import fileinput
import collections

L = list([l.strip() for l in fileinput.input()])

c = 0
w = ""
for i, l in enumerate(L):
	if l != "":
		w += l
	else:
		c += len(collections.Counter(w).keys())
		w = ""
		P = {}

	if i == len(L) - 1 and l != "":
		c += len(collections.Counter(w).keys())

print (c)

P2 = {}
c = 0
k = 0
for i, l in enumerate(L):
	if l != "":
		w = l
		P1 = collections.Counter(w)
		for p in P1:
			if p in P2:
				P2[p] += P1[p]
			else:
				P2[p] = 1
		k += 1
	else:
		for p in P2:
			if P2[p] == k:
				c += 1
		P2 = {}
		k = 0

	if i == len(L) - 1 and l != "":
		for p in P2:
			if P2[p] == k:
				c += 1

print (c)

# Sol input6.dat
#
# 6542
# 3299
#
# Time: 0.020 s
