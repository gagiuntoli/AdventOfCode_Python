import fileinput
import collections

def con1(w):
	ws = str(w)
	if len(ws) != 6:
		return False
	rep = False
	inc = True
	for i in range(0, len(ws)-1):
		if ws[i] > ws[i+1]:
			inc = False
	M = collections.Counter(ws)
	rep = False
	for m in M:
		if M[m] >= 2:
			rep = True
	return rep and inc

def con2(w):
	ws = str(w)
	if len(ws) != 6:
		return False
	inc = True
	for i in range(0, len(ws)-1):
		if ws[i] > ws[i+1]:
			inc = False
	M = collections.Counter(ws)
	rep = False
	for m in M:
		if M[m] == 2:
			rep = True
	return rep and inc
	

L = list([l.strip() for l in fileinput.input()])

a = int(L[0].split('-')[0])
b = int(L[0].split('-')[1])

count1 = 0
count2 = 0
for w in range(a, b):
	if con1(w):
		count1 += 1
	if con2(w):
		count2 += 1
print (count1)
print (count2)

# Sol input4.dat
#
# 945
# 617
#
# Time: 1.963 s
