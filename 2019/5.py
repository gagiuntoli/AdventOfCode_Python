import fileinput

def run(code, inp):

	i = 0
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
			code[p1] = inp
			i += 2
		elif op == 4:
			p1 = code[i+1]
			a = code[p1] if m1 == 0 else p1
			out = a
			i += 2
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
			return out


L = list([l.strip() for l in fileinput.input()])

code = [int(x) for x in L[0].split(',')]
print(run(code, 1))

code = [int(x) for x in L[0].split(',')]
print(run(code, 5))

# Comparison tests
# Position mode
for i in range (0, 20):
	code = [3,9,8,9,10,9,4,9,99,-1,8]
	assert run(code,i) == (1 if i == 8 else 0), "failed for i = " + str(i)
for i in range (0, 20):
	code = [3,9,7,9,10,9,4,9,99,-1,8]
	assert run(code,i) == (1 if i < 8 else 0), "failed for i = " + str(i)

# Inmediate mode
for i in range (0, 20):
	code = [3,3,1108,-1,8,3,4,3,99]
	assert run(code,i) == (1 if i == 8 else 0), "failed for i = " + str(i)
for i in range (0, 20):
	code = [3,3,1107,-1,8,3,4,3,99]
	assert run(code,i) == (1 if i < 8 else 0), "failed for i = " + str(i)

# Jump instruction tests
# Position mode
code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
assert run(code, 0) == 0, "test jump instructions"
code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
assert run(code, 1) == 1, "test jump instructions"

# Inmediate mode
code = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
assert run(code, 0) == 0, "test jump instructions"
code = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
assert run(code, 1) == 1, "test jump instructions"

# Large example
for i in range (20):
	code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,  \
		98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000, \
		1,20,4,20,1105,1,46,98,99]
	if i < 8:
		assert run(code, i) == 999
	elif i == 8:
		assert run(code, i) == 1000
	elif i > 8:
		assert run(code, i) == 1001
	
# Sol input5.dat
#
# 4887191
# 3419022
#
# Time: 0.016 s
