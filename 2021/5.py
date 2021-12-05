import fileinput
from collections import defaultdict

L = [l.strip() for l in fileinput.input()]

def add_points(POINTS, line, diagonals=False):
	for x1, y1, x2, y2 in lines:
		x_range = range(x1, x2 + (1 if x1 <= x2 else -1), 1 if x1 <= x2 else -1)
		y_range = range(y1, y2 + (1 if y1 <= y2 else -1), 1 if y1 <= y2 else -1)
		if y1 == y2:
			for x in x_range:
				POINTS[(x,y1)] += 1
		elif x1 == x2:
			for y in y_range:
				POINTS[(x1,y)] += 1
		elif diagonals:
			for x,y in zip(x_range, y_range):
				POINTS[(x,y)] += 1

lines = []
for line in L:
	line = line.split(" ")
	line_aux = line[0].split(",") + line[2].split(",")
	line_aux = [int(x) for x in line_aux]
	lines.append(line_aux)

POINTS = defaultdict(int)
add_points(POINTS,lines)
print(sum(value > 1 for value in POINTS.values()))

POINTS = defaultdict(int)
add_points(POINTS,lines, diagonals=True)
print(sum(value > 1 for value in POINTS.values()))
		
	
# Sol input .dat
#
# 5294
# 21698
#
# Time: 0.18 s
