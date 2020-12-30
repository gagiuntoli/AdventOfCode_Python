import fileinput

L = list([l.strip() for l in fileinput.input()])

def fuel1(m):
	return m // 3 - 2

def fuel2(m):
	s = 0
	while m > 0:
		m = m // 3 - 2
		if m > 0:	
			s += m
	return s

s1 = 0
s2 = 0
for l in L:
	n = fuel1(int(l))
	s1 += n
	n = fuel2(int(l))
	s2 += n

print (s1)
print (s2)

# Sol input1.dat
#
# 3226822
# 4837367
#
# Time: 0.014 s
