import fileinput

L = list([l.strip() for l in fileinput.input()])

def computer(L):
	D = {}
	acc = 0
	i = 0
	while i < len(L):
		l = L[i].split()
		if i in D:
			return acc, -1
		D[i] = True
		if l[0] == "acc":
			acc += int(l[1])
			i += 1
		elif l[0] == "jmp":
			i += int(l[1])
		elif l[0] == "nop":
			i += 1
	return acc, 0

print(computer(L)[0])

for i, l in enumerate(L):
	if L[i][:3] == "jmp":
		L[i] = "nop" + L[i][3:]
		if computer(L)[1] == 0:
			sol = computer(L)[0] 
			break
		L[i] = "jmp" + L[i][3:]
	if L[i][:3] == "nop":
		L[i] = "jmp" + L[i][3:]
		if computer(L)[1] == 0:
			sol = computer(L)[0] 
			break
		L[i] = "nop" + L[i][3:]
print(sol)

# Sol input8.dat
#
# 1753
# 733
#
# Time: 0.017 s
