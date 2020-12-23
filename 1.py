import fileinput

L = list([l.strip() for l in fileinput.input()])

enter_basement = False
floor = 0
for p, i in enumerate(L[0]):
	if i == '(':
		floor += 1
	elif i == ')':
		floor -= 1
	if floor == -1 and enter_basement == False:
		basement = p
		enter_basement = True
	

print (floor)
print (basement + 1)
