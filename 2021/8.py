import fileinput
L = [l.strip() for l in fileinput.input()]

def decode(numbers, D):
	num = 0
	for i,d in enumerate(numbers):
		num += D[d] * (10**(3-i))
	return num

def find_non_repeated(a, b):
	if len(b) > len(a):
		a, b = b, a
	res = ""
	for c in a:
		res += c if c not in b else ""
	return res

def decode_table(numbers):
	DI = {}
	for n in numbers:
		if len(n) in [2,3,4,7]:
			DI[{2:1, 3:7, 4:4, 7:8}[len(n)]] = n
	cf = DI[1]
	a = find_non_repeated(DI[7], DI[1]) # a = 7 - 1
	bd = find_non_repeated(DI[4], DI[1]) # bd = 4 - 1

	for n in numbers:
		if len(n) == 5: # opt: 2, 3, 5
			if all(x in n for x in cf):
				DI[3] = n
			elif all(x in n for x in bd):
				DI[5] = n
			else:
				DI[2] = n
		if len(n) == 6: # opt: 0, 6, 9
			if not all(x in n for x in bd):
				DI[0] = n		
			elif all(x in n for x in cf):
				DI[9] = n
			else:
				DI[6] = n
	D = {}
	for i in DI:
		D[DI[i]] = i
	return D

count1 = 0
count2 = 0
for line in L:
	line = line.split(" ")

	for i, l in enumerate(line):
		line[i] = "".join(sorted(l))

	count1 += sum(len(x) in [2,3,4,7] for x in line[11:15])
	D = decode_table(line[0:10] + line[11:15])
	
	count2 += decode(line[11:15], D)

print(count1)
print(count2)

# Sol input .dat
#
# 514
# 1012272
#
# Time: 0.048 s
