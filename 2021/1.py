import fileinput
from collections import defaultdict

L = [int(x) for x in list([l.strip() for l in fileinput.input()])]

count = 0
for i in range(1,len(L)):
	if L[i] > L[i-1]:
		count += 1
print(count)

countW = 0
for i in range(2,len(L)):
	currW = L[i] + L[i-1] + L[i-2]
	if i > 2 and currW > prevW:
		countW += 1
	prevW = currW
print(countW)


# Sol input1.dat
#
# 1583
# 1627
#
# Time: 0.019 s
