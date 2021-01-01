import fileinput
import collections

L = list([l.strip() for l in fileinput.input()])

def check2(w1, w2):
	W1 = collections.Counter(w1)
	W2 = collections.Counter(w2)
	for i in W1:
		if not i in W2:
			return True
	for i in W2:
		if not i in W1:
			return True
	return False
	

count = 0
for l in L:
	l = l.split()
	W = {}
	valid = True
	for k in l:
		if k in W:
			valid = False
		else:
			W[k] = True
	if valid:
		count += 1
		
print(count)

count = 0
for l in L:
	l = l.split()
	valid = True
	for k in range(0, len(l) - 1):
		for m in range(k + 1, len(l)):
			if not check2(l[k], l[m]):
				valid = False
	if valid:
		count += 1
		
print(count)

# Sol input4.dat
#
# 455
# 186
#
# Time: 0.075 s
