import fileinput

L = list([l.strip() for l in fileinput.input()])

f = L[0]

def react(f):
	change = True
	p = - ord('a') + ord('A')
	while change:
		change = False
		for l in range(0, len(f)-1):
			if ord(f[l]) == ord(f[l+1]) + p or ord(f[l]) + p == ord(f[l+1]):
				f = f[0:l] + f[l+2:]
				change = True
				break
	return f

f = react(f)
print (len(f))

min_fc = 10000000000000000
for i in range(26):
	fc = f
	a = chr(i + ord('a'))
	A = chr(i + ord('A'))
	fc = fc.replace(a, '')
	fc = fc.replace(A, '')
	fc = react(fc)
	if len(fc) < min_fc:
		min_fc = len(fc)

print(min_fc)

	
# Sol input5.dat
#
# 9562
# 4934
#
# Time: 25.34 s
