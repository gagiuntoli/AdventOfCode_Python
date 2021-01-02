import fileinput

L0 = list([l.strip() for l in fileinput.input()])

for i in range(0, len(L0)):
	L0[i] = int(L0[i])

L = L0.copy()
count = 0
i = 0
while True:
	if i >= len(L):
		break
	L[i] += 1
	i += L[i] - 1
	count += 1
		
print(count)

L = L0.copy()
count = 0
i = 0
while True:
	if i >= len(L):
		break
	if L[i] >= 3:
		L[i] -= 1
		i += L[i] + 1
	else:
		L[i] += 1
		i += L[i] - 1
	count += 1

print(count)

# Sol input5.dat
#
# 358131
# 25558839
#
# Time: 6.620 s
