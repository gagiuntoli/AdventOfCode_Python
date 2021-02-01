import fileinput
from collections import defaultdict

def run(code, inp):

	rel_base = 0
	out = []
	i = 0
	while True:
		inst = str(code[i])
		inst_a = ""
		for j in range(5 - len(inst)):
			inst_a += "0"
		inst = inst_a + inst
		assert len(inst) == 5
		m1 = int(inst[2])
		m2 = int(inst[1])
		m3 = int(inst[0])
		op = int(inst[3:5])

		if m1 == 0:
			p1 = code[i+1]
		elif m1 == 1:
			p1 = i+1
		elif m1 == 2:
			p1 = rel_base + code[i+1]

		if m2 == 0:
			p2 = code[i+2]
		elif m2 == 1:
			p2 = i+2
		elif m2 == 2:
			p2 = rel_base + code[i+2]

		if m3 == 0:
			p3 = code[i+3]
		elif m3 == 1:
			p3 = i+3
		elif m3 == 2:
			p3 = rel_base + code[i+3]

		if op == 1:
			code[p3] = code[p1] + code[p2]
			i += 4
		elif op == 2:
			code[p3] = code[p1] * code[p2]
			i += 4
		elif op == 3:
			code[p1] = inp
			i += 2
		elif op == 4:
			out.append(code[p1])
			i += 2
		elif op == 5:
			if code[p1] != 0:
				i = code[p2]
			else:
				i += 3
		elif op == 6:
			if code[p1] == 0:
				i = code[p2]
			else:
				i += 3
		elif op == 7:
			code[p3] = 1 if code[p1] < code[p2] else 0
			i += 4
		elif op == 8:
			code[p3] = 1 if code[p1] == code[p2] else 0
			i += 4
		elif op == 9:
			rel_base += code[p1]
			i += 2
		elif op == 99:
			return out
		else:
			print("invalid opcode")


L = list([l.strip() for l in fileinput.input()])
code_0 = defaultdict(lambda:0)

for i, l in enumerate(L[0].split(",")):
	code_0[i] = int(l)

print(run(code_0.copy(), 1))
print(run(code_0.copy(), 2))

# Sol input9.dat
#
# 4234906522 
# 60962
#
# Time: 0.467 s
