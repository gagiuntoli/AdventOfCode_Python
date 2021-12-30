import fileinput

L = [int(x) for x in list([l.strip() for l in fileinput.input()])]

count = 0
for i in range(1,len(L)):
	if L[i] > L[i-1]:
		count += 1
print(count)

count = 0
for i in range(1,len(L)-2):
	if L[i+2] > L[i-1]:
		count += 1
print(count)


# Sol input1.dat
#
# 1583
# 1627
#
# Time: 0.019 s
