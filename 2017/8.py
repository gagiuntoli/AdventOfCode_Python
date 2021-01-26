import fileinput
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])

R = defaultdict(lambda:0)

def condition_valid(con_reg, con_op, con_num):
	if con_op == "<":
		return R[con_reg] < con_num
	elif con_op == "<=":
		return R[con_reg] <= con_num
	elif con_op == ">":
		return R[con_reg] > con_num
	elif con_op == ">=":
		return R[con_reg] >= con_num
	elif con_op == "==":
		return R[con_reg] == con_num
	elif con_op == "!=":
		return R[con_reg] != con_num
	else:
		print("invalid comparison operation")
		return False

def modify_register(reg, op, num):
	if op == "inc":
		R[reg] += num
	elif op == "dec":
		R[reg] -= num
	else:
		print("invalid operation")

max_h = -10000000000000000
for l in L:
	l = l.split("if")
	reg = l[0].split()[0]
	op = l[0].split()[1]
	num = int(l[0].split()[2])
	con_reg = l[1].split()[0]
	con_op = l[1].split()[1]
	con_num = int(l[1].split()[2])
	if condition_valid(con_reg, con_op, con_num):
		modify_register(reg, op, num)
	max_h = max(max_h, max(R.values()))

max_r = max(R.values())
	
print(max_r)
print(max_h)
	

# Sol input7.dat
#
# 5143
# 6209 
#
# Time: 0.016 s
