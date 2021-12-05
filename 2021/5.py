import fileinput
from collections import defaultdict

L = [l.strip() for l in fileinput.input()]

def is_vertical(line):
	return True if line[0] == line[2] else False

def is_horizontal(line):
	return True if line[1] == line[3] else False

def add_points(POINTS, line):
	if is_vertical(line):
		if line[1] <= line[3]:
			for i in range(line[1],line[3]+1):
				POINTS[(line[0],i)] += 1
		else:
			for i in range(line[1],line[3]-1,-1):
				POINTS[(line[0],i)] += 1
	elif is_horizontal(line):
		if line[0] <= line[2]:
			for i in range(line[0],line[2]+1):
				POINTS[(i,line[1])] += 1
		else:
			for i in range(line[0],line[2]-1,-1):
				POINTS[(i,line[1])] += 1

def add_points_with_diagonal(POINTS, line):
	if is_vertical(line):
		if line[1] <= line[3]:
			for i in range(line[1],line[3]+1):
				POINTS[(line[0],i)] += 1
		else:
			for i in range(line[1],line[3]-1,-1):
				POINTS[(line[0],i)] += 1
	elif is_horizontal(line):
		if line[0] <= line[2]:
			for i in range(line[0],line[2]+1):
				POINTS[(i,line[1])] += 1
		else:
			for i in range(line[0],line[2]-1,-1):
				POINTS[(i,line[1])] += 1
	else:
		assert (abs(line[0] - line[2]) == abs(line[1] - line[3]))
		if line[0] <= line[2] and line[1] <= line[3]:
			for i in range(line[2] - line[0]+1):
				POINTS[(line[0]+i,line[1]+i)] += 1
		elif line[0] <= line[2] and line[1] > line[3]:
			for i in range(line[2] - line[0]+1):
				POINTS[(line[0]+i,line[1]-i)] += 1
		elif line[0] > line[2] and line[1] > line[3]:
			for i in range(line[0] - line[2]+1):
				POINTS[(line[0]-i,line[1]-i)] += 1
		elif line[0] > line[2] and line[1] <= line[3]:
			for i in range(line[0] - line[2]+1):
				POINTS[(line[0]-i,line[1]+i)] += 1

lines = []
for line in L:
	line = line.split(" ")
	line_aux = line[0].split(",") + line[2].split(",")
	line_aux = [int(x) for x in line_aux]
	lines.append(line_aux)

POINTS = defaultdict(int)

for line in lines:
	add_points(POINTS,line)

count = 0
for point in POINTS.keys():
	if POINTS[point] > 1:
		count += 1
print(count)

POINTS = defaultdict(int)
for line in lines:
	add_points_with_diagonal(POINTS,line)

count = 0
for point in POINTS.keys():
	if POINTS[point] > 1:
		count += 1

print(count)
		
	
# Sol input .dat
#
# 5294
# 21698
#
# Time: 0.18 s
