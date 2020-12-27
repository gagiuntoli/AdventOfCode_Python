import fileinput

L = list([l.strip() for l in fileinput.input()])

area = 0
perimeter = 0
for l in L:
	s = [int(x) for x in l.split('x')]
	s.sort()
	
	print (s, min(s))
	a1 = s[0]*s[1] 
	a2 = s[0]*s[2] 
	a3 = s[2]*s[1]
	area += 2*a1 + 2*a2 + 2*a3 + min(a1, a2, a3)
	perimeter += 2*s[0] + 2*s[1] + s[0]*s[1]*s[2]
	

print (area)
print (perimeter)
