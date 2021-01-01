import fileinput
import collections

L = list([l.strip() for l in fileinput.input()])

count1 = 0
count2 = 0
for l in L:
	l = l.split()
	a = int(l[0].split('-')[0])
	b = int(l[0].split('-')[1])
	letter = l[1][0]
	w = l[2]
	W = collections.Counter(w)
	if a <= W[letter] and W[letter] <= b:
		count1 += 1
	if (w[a-1] == letter and w[b-1] != letter) or (w[a-1] != letter and w[b-1] == letter):
		count2 += 1

print (count1)
print (count2)

# Sol input2.dat
#
# 506
# 443
#
# Time: 0.018 s
