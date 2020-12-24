import fileinput

L = list([l.strip() for l in fileinput.input()])

size = 1000
grid = [[False for y in range(size)] for x in range(size)]
grid2 = [[0 for y in range(size)] for x in range(size)]

for l in L:
	l = l.split()
	index = 0 if (l[0] == 'toggle') else 1

	state = l[index]
	coor1 = [int(x) for x in l[index + 1].split(',')]
	coor2 = [int(x) for x in l[index + 3].split(',')]
	for i in range(coor1[0], coor2[0] + 1):
		for j in range(coor1[1], coor2[1] + 1):
			if state == 'on':
				grid[i][j] = True
				grid2[i][j] += 1
			elif state == 'off':
				grid[i][j] = False
				if (grid2[i][j] > 0):
					grid2[i][j] -= 1
			elif state == 'toggle':
				grid[i][j] = True if grid[i][j] == False else False
				grid2[i][j] += 2
			else:
				print ("invalid option ", state)

count = 0
for i in range(size):
	for j in range(size):
		if grid[i][j] == True:
			count += 1

bright = 0
for i in range(size):
	for j in range(size):
		bright += grid2[i][j]

print (count)
print (bright)
		
