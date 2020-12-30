import fileinput

L = list([l.strip() for l in fileinput.input()])

P = []
for l in L:
	P.append(int(l))

for p in range(0, len(P) - 1):
	for k in range(p + 1, len(P)):
		if P[p] + P[k] == 2020:
			num = P[p] * P[k]
print (num)

for p in range(0, len(P) - 1):
	for k in range(p + 1, len(P)):
		for m in range(p + 1, len(P)):
			if P[p] + P[k] + P[m] == 2020:
				num = P[p] * P[k] * P[m]
print (num)

# Sol input1.dat
#
# 290784
# 177337980
#
# Time: 0.362 s
