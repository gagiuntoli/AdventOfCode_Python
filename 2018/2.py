import fileinput
import collections

L = list([l.strip() for l in fileinput.input()])

def similar(w1, w2):
	c = 0
	for i in range(0, len(w1)):
		if w1[i] == w2[i]:
			c += 1
	if c == len(w1) - 1:
		return True
	return False

s2 = 0
s3 = 0
for l in L:
	P = collections.Counter(l)
	s2f = False
	s3f = False
	for i in P:
		if P[i] == 2:
			s2f = True
		if P[i] == 3:
			s3f = True
	if s2f:
		s2 += 1
	if s3f:
		s3 += 1

print (s2 * s3)

for m in range(0, len(L)):
	for k in range(m + 1, len(L)):
		w = ""
		if similar(L[m], L[k]):
			for i in range(0, len(L[m])):
				if L[m][i] == L[k][i]:
					w += L[m][i]
			print (w)	

# Sol input2.dat
#
# 5880
# tiwcdpbseqhxryfmgkvjujvza
#
# Time: 0.111 s
