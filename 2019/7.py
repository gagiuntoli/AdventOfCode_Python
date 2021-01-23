import fileinput
from itertools import permutations  

def run(code, inp, i):

	out = None
	while i < len(code):
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
		assert m3 == 0, "m3 != 0"

		if op == 1:
			p1 = code[i+1]
			p2 = code[i+2]
			p3 = code[i+3]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			code[p3] = a + b
			i += 4
		elif op == 2:
			p1 = code[i+1]
			p2 = code[i+2]
			p3 = code[i+3]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			code[p3] = a * b
			i += 4
		elif op == 3:
			p1 = code[i+1]
			code[p1] = inp.pop(0)
			i += 2
		elif op == 4:
			p1 = code[i+1]
			a = code[p1] if m1 == 0 else p1
			out = a
			i += 2
			return out, i
		elif op == 5:
			p1 = code[i+1]
			p2 = code[i+2]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			if a != 0:
				i = b
			else:
				i += 3
		elif op == 6:
			p1 = code[i+1]
			p2 = code[i+2]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			if a == 0:
				i = b
			else:
				i += 3
		elif op == 7:
			p1 = code[i+1]
			p2 = code[i+2]
			p3 = code[i+3]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			code[p3] = 1 if a < b else 0
			i += 4
		elif op == 8:
			p1 = code[i+1]
			p2 = code[i+2]
			p3 = code[i+3]
			a = code[p1] if m1 == 0 else p1
			b = code[p2] if m2 == 0 else p2
			code[p3] = 1 if a == b else 0
			i += 4
		elif code[i] == 99:
			return None, i


L = list([l.strip() for l in fileinput.input()])
code_0 = [int(x) for x in L[0].split(',')]

def amplificator(code_0):
	perm = permutations([0, 1, 2, 3, 4])  
	max_out = -1000000
	for p in perm:
		out = 0
		for i in p:
			inp = [i, out]
			code = code_0.copy()
			out, pc = run(code, inp, 0)
		max_out = max(max_out, out)

	return max_out

def amplificator_feedback(code_0):
	# For this part it is important to store the program counter
	# since the computers should remain "paused"
	perm = permutations([5, 6, 7, 8, 9])  
	max_out = -1000000
	out_val = 0
	for p in perm:
		codes = []
		for i in p:
			codes.append((code_0.copy(), 0))
		out = 0
		out_val = out
		for ix, i in enumerate(p):
			inp = [i, out]
			out, pc = run(codes[ix][0], inp, codes[ix][1])
			codes[ix] = (codes[ix][0], pc)
		out_val = out if out != None else out_val
		while out != None:
			for ix, i in enumerate(p):
				inp.append(out)
				out, pc = run(codes[ix][0], inp, codes[ix][1])
				codes[ix] = (codes[ix][0], pc)
			out_val = out if out != None else out_val
		max_out = max(max_out, out_val)

	return max_out

print (amplificator(code_0))
print (amplificator_feedback(code_0))

# Sol input5.dat
#
# 262086
# 5371621
#
# Time: 0.046 s
