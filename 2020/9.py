import fileinput

L = [int(x) for x in list([l.strip() for l in fileinput.input()])]

def is_sum(D, s):
	for i in range(len(D) - 1):
		if s - D[i] in D:
			return True
	return False

def find_contiguous(L, num):
	a = 0
	b = 0
	s = L[a]
	while b < len(L):
		if s < num:
			b += 1
			s += L[b]
		elif s > num:
			s -= L[a]
			a += 1
		else:
			minimum = min([L[x] for x in range(a,b+1)])
			maximum = max([L[x] for x in range(a,b+1)])
			return minimum + maximum
	return None

D = [L[i] for i in range(25)]
i = 25
while i < len(L):
	if not is_sum(D, L[i]):
		sol = L[i]
		break
	D.append(L[i])
	D.pop(0)
	i += 1

print(sol)

print(find_contiguous(L, sol))

# Sol input9.dat
#
# 393911906
# 59341885
#
# Time: 0.016 s
