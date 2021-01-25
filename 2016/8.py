import fileinput

L = list([l.strip() for l in fileinput.input()])

width = 50
height = 6
grid = [["." for i in range(width)] for j in range(height)]

for l in L:
	l = l.split()
	if l[0] == "rect":
		a = int(l[1].split("x")[0])
		b = int(l[1].split("x")[1])
		for i in range(b):
			for j in range(a):
				grid[i][j] = "#"
	elif l[0] == "rotate":
		if l[1] == "column":
			col = int(l[2][2:])
			rot = int(l[4])
			copy = []
			for i in range(height):
				copy.append(grid[i][col])
			for i in range(height):
				grid[i][col] = copy[(i - rot) % height]
		elif l[1] == "row":
			row = int(l[2][2:])
			rot = int(l[4])
			copy = []
			for i in range(width):
				copy.append(grid[row][i])
			for i in range(width):
				grid[row][i] = copy[(i - rot) % width]
		else:
			print("Invalid instruction")
	else:
		print("Invalid instruction")

count = 0
for i in range(height):
	for j in range(width):
		if grid[i][j] == '#':
			count += 1
print(count)
for i in grid:
	v = ""
	for j in i:
		v += j
	print (v)

# Sol input8.dat
#
# 110
# ZJHRKCPLYJ
#
# Time: 0.016 s
