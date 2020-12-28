import fileinput

L = list([l.strip() for l in fileinput.input()])

def valid_tri(s):
	if s[0] + s[1] > s[2] and s[1] + s[2] > s[0] and s[0] + s[2] > s[1]:
		return True
	return False

valid = 0
for t in L:
	t = [int(x) for x in t.split()]
	if valid_tri(t):
		valid += 1
	
print (valid)

t1 = [0] * 3
t2 = [0] * 3
t3 = [0] * 3

valid = 0
for i in range(0, len(L)):
	t = [int(x) for x in L[i].split()]
	
	t1[i % 3] = t[0]
	t2[i % 3] = t[1]
	t3[i % 3] = t[2]

	if i != 0 and (i + 1) % 3 == 0:
		if valid_tri(t1):
			valid += 1
		if valid_tri(t2):
			valid += 1
		if valid_tri(t3):
			valid += 1

print (valid)
