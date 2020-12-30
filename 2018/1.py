import fileinput

L = list([l.strip() for l in fileinput.input()])

s = 0
for l in L:
	n = int(l)
	s += n

print (s)

s = 0
F = {}
f_flag = False
while not f_flag:
	for l in L:
		F[s] = True
		n = int(l)
		s += n
		if (not f_flag) and (s in F):
			f_rep = s
			f_flag = True

print (f_rep)
