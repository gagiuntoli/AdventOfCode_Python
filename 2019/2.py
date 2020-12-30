import fileinput

def run(code):
	for i in range(0, len(code), 4):
		if code[i] == 1:
			code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
		elif code[i] == 2:
			code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
		elif code[i] == 99:
			return code[0]

L = list([l.strip() for l in fileinput.input()])

code = [int(x) for x in L[0].split(',')]

code[1] = 12
code[2] = 2

print(run(code))

for n in range(0, 100):
	for v in range(0, 100):
		code = [int(x) for x in L[0].split(',')]
		code[1] = n
		code[2] = v
		if run(code) == 19690720:
			sol = 100 * n + v

print(sol)

# Sol input2.dat
#
# 2692315
# 9507
#
# Time: 0.181 s
