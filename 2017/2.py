import fileinput

L = list([l.strip() for l in fileinput.input()])

s = 0
for l in L:
	l = [int(x) for x in l.split()]
	s += max(l) - min(l)
print (s)

s = 0
for l in L:
	l = [int(x) for x in l.split()]
	for i in l:
		for j in l:
			if i != j:
				if i % j == 0:
					s += int(i / j)
print (s)

# Sol input2.dat
#
# 47623
# 312
#
# Time: 0.015 s
