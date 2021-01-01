import fileinput

L = list([l.strip() for l in fileinput.input()])

slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

mult = 1
for s in slope:
	width = len(L[0])
	R = s[0]
	D = s[1]
	r = 0
	d = 0
	count = 0
	while d < len(L):
		if L[d][r] == '#':
			count += 1
		d += D	
		r = (r + R) % width	
	
	if s == [3, 1]:
		count1 = count
	mult *= count

print (count1)
print (mult)

# Sol input3.dat
#
# 151
# 7540141059
#
# Time: 0.014 s
