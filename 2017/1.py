import fileinput

L = list([l.strip() for l in fileinput.input()])

n = L[0]

s = 0
for i in range(0, len(n)):
	if n[i] == n[(i+1) % len(n)]:
		s += int(n[i])
print (s)

s = 0
for i in range(0, len(n)):
	if n[i] == n[(i+len(n)//2) % len(n)]:
		s += int(n[i])
print (s)
