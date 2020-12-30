# Conway Sequence Generator

import fileinput

def transform(num):
	num_new = ""
	i = 0
	while i < len(num):
		rep = 1
		while i+rep < len(num):
			if num[i] != num[i+rep]:
				break
			rep += 1
		num_new += str(rep)+num[i]
		i += rep
	return num_new
		
		
L = list([l.strip() for l in fileinput.input()])

num = L[0]
for i in range(40):
	num = transform(num)
print (len(num))

num = L[0]
for i in range(50):
	num = transform(num)
print (len(num))

# Sol input10.dat
#
# 492982
# 6989950
#
# Time: 7.205 s
