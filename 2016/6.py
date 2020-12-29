import fileinput

L = list([l.strip() for l in fileinput.input()])

P = []
for i in range(len(L[0])):
	P.append({})

for l in L:
	for j in range(0, len(l)):
		if not l[j] in P[j].keys():
			P[j][l[j]] = 1
		else:
			P[j][l[j]] += 1

password1 = ""
password2 = ""
for p in P:
	min_val = 100000000
	max_val = 0
	max_let = ""
	for j in p.keys():
		if p[j] > max_val:
			max_val = p[j]
			max_let = j
		if p[j] < min_val:
			min_val = p[j]
			min_let = j
	password1 += max_let
	password2 += min_let

print(password1)
print(password2)
