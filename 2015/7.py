import fileinput

def solve_wires(L, key_to_search, b_fixed = False):

	keys = memory.keys()
	
	while not key_to_search in keys:
		for l in L:
			l = l.split()
			can_operate_1 = False
			can_operate_2 = False
			if 'NOT' in l:
				var1 = l[1]
				var_s = l[3]
		
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
	
				if can_operate_1:	
					memory[var_s] = ~op1
		
			elif 'AND' in l:
				var1 = l[0]
				var2 = l[2]
				var_s = l[4]
		
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
		
				if var2.isnumeric():
					op2 = int(var2)
					can_operate_2 = True
				elif var2 in keys:
					op2 = int(memory[var2])
					can_operate_2 = True
		
				if can_operate_1 and can_operate_2:	
					memory[var_s] = op1 & op2
		
			elif 'OR' in l:
				var1 = l[0]
				var2 = l[2]
				var_s = l[4]
		
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
		
				if var2.isnumeric():
					op2 = int(var2)
					can_operate_2 = True
				elif var2 in keys:
					op2 = int(memory[var2])
					can_operate_2 = True
		
				if can_operate_1 and can_operate_2:	
					memory[var_s] = op1 | op2
		
			elif 'LSHIFT' in l:
				var1 = l[0]
				shift = l[2]
				var_s = l[4]
		
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
		
				if can_operate_1:
					memory[var_s] = op1 << int(shift)
		
			elif 'RSHIFT' in l:
				var1 = l[0]
				shift = l[2]
				var_s = l[4]
		
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
		
				if can_operate_1:
					memory[var_s] = op1 >> int(shift)
		
			else:
				var1 = l[0]
				var_s = l[2]
	
				if var1.isnumeric():
					op1 = int(var1)
					can_operate_1 = True
				elif var1 in keys:
					op1 = int(memory[var1])
					can_operate_1 = True
		
				if can_operate_1 and (not b_fixed or var_s != 'b'):
					memory[var_s] = op1
				
			keys = memory.keys()

# Init

L = list([l.strip() for l in fileinput.input()])

memory = {} 
key_to_search = 'a' 

solve_wires(L, key_to_search)
print (memory[key_to_search])

b_value = memory[key_to_search]
memory = {'b': b_value} 
solve_wires(L, key_to_search, True)
print (memory[key_to_search])
