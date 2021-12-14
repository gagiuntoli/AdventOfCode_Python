import fileinput
from collections import defaultdict

L = [l.strip().split() for l in fileinput.input()]

W = L[0][0]
F = {}
for line in L:
	if "->" in line:
		F[line[0]] = line[2]

def count_max_min(PAIRS,END):
	C = defaultdict(int)
	C[END] += 1
	for p in PAIRS:
		C[p[0]] += PAIRS[p]
	Max = max(C.values())
	Min = min(C.values())
	return Min, Max

PAIRS = defaultdict(int)
for i in range(len(W)-1):
	PAIRS[W[i:i+2]] += 1

for i in range(40):
	BLOCKED = defaultdict(int)
	PAIRS_keys = list(PAIRS.keys())
	for p in PAIRS_keys:
		diff = PAIRS[p] - BLOCKED[p]
		if PAIRS[p] > 0 and p in F and 0 < diff:
			PAIRS[p] -= diff
			s1 = p[0] + F[p]
			s2 = F[p] + p[1]
			PAIRS[s1] += diff
			PAIRS[s2] += diff
			BLOCKED[s1] += diff
			BLOCKED[s2] += diff
	if i == 9:
		Min, Max = count_max_min(PAIRS,W[-1])
		P1 = Max - Min
	if i == 39:
		Min, Max = count_max_min(PAIRS,W[-1])
		P2 = Max - Min

print(P1)
print(P2)


# Sol input14.dat
#
# 2027
# 2265039461737
#
# Time: 0.05 s
