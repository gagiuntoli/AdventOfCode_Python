import fileinput
from collections import defaultdict

L0 = [l.strip() for l in fileinput.input()]

def occupied_neighbours(L, x, y):
	width = len(L[0])
	height = len(L)
	neighbours = [[x+1,y],
		     [x+1,y+1],		
		     [x,y+1],		
		     [x-1,y+1],		
		     [x-1,y],		
		     [x-1,y-1],		
		     [x,y-1],		
		     [x+1,y-1]]

	count = 0
	for v in neighbours:
		if 0 <= v[0] and v[0] < width and 0 <= v[1] and v[1] < height:
			if L[v[1]][v[0]] == '#':
				count += 1
	return count

def occupied_visible_neighbours(L, x, y):
	width = len(L[0])
	height = len(L)
	directions = [[1,0],
		      [1,1],		
		      [0,1],		
		      [-1,1],		
		      [-1,0],		
		      [-1,-1],		
		      [0,-1],		
		      [1,-1]]

	count = 0
	for d in directions:
		i = 1
		while True:
			x1 = x + d[0] * i
			y1 = y + d[1] * i
			if 0 <= x1 and x1 < width and 0 <= y1 and y1 < height:
				if L[y1][x1] == '#':
					count += 1
					break
				elif L[y1][x1] == 'L':
					break
			else:
				break
			i += 1
	return count

def evolute(L, prob):
	L0 = L.copy()
	width = len(L0[0])
	height = len(L0)
	if prob == 1:
		for i in range(height):
			string = ""
			for j in range(width):
				if L0[i][j] == 'L' and occupied_neighbours(L0, j, i) == 0:
					string += '#'
				elif L0[i][j] == '#' and occupied_neighbours(L0, j, i) >= 4:
					string += 'L'
				else:
					string += L0[i][j]
			L[i] = string
	elif prob == 2:
		for i in range(height):
			string = ""
			for j in range(width):
				if L0[i][j] == 'L' and \
				   occupied_visible_neighbours(L0, j, i) == 0:
					string += '#'
				elif L0[i][j] == '#' and \
				   occupied_visible_neighbours(L0, j, i) >= 5:
					string += 'L'
				else:
					string += L0[i][j]
			L[i] = string
	else:
		print("Error: problem type", prob, "not defined")

def occupied(L, prob):
	L0 = L.copy()
	evolute(L, prob)
	while L != L0:
		L0 = L.copy()
		evolute(L, prob)

	count = 0
	for l in L:
		count += l.count('#')
	return count

print(occupied(L0.copy(), 1))
print(occupied(L0.copy(), 2))

L = ['###',
     '###',
     '###']
assert occupied_neighbours(L, 1, 1) == 8
assert occupied_neighbours(L, 0, 0) == 3
assert occupied_neighbours(L, 2, 1) == 5
assert occupied_neighbours(L, 2, 2) == 3

L = ['L#.',
     '#L#',
     'L,#']
assert occupied_neighbours(L, 1, 1) == 4
assert occupied_neighbours(L, 0, 0) == 2
assert occupied_neighbours(L, 2, 1) == 2
assert occupied_neighbours(L, 2, 2) == 1

L = ['LLL',
     'LLL',
     'LLL']
assert occupied_neighbours(L, 1, 1) == 0
assert occupied_neighbours(L, 0, 0) == 0
assert occupied_neighbours(L, 2, 1) == 0
assert occupied_neighbours(L, 2, 2) == 0

L = ['LLL',
     'LLL',
     'LLL']
assert occupied_visible_neighbours(L, 1, 1) == 0
assert occupied_visible_neighbours(L, 0, 0) == 0
assert occupied_visible_neighbours(L, 2, 1) == 0
assert occupied_visible_neighbours(L, 2, 2) == 0

L = ['LLL',
     'LLL',
     'LLL']
evolute(L, 1)
assert L == ['###', '###', '###']

L0 = ['L.LL.LL.LL',
      'LLLLLLL.LL',
      'L.L.L..L..',
      'LLLL.LL.LL',
      'L.LL.LL.LL',
      'L.LLLLL.LL',
      '..L.L.....',
      'LLLLLLLLLL',
      'L.LLLLLL.L',
      'L.LLLLL.LL']

L1 = ['#.##.##.##',
      '#######.##',
      '#.#.#..#..',
      '####.##.##',
      '#.##.##.##',
      '#.#####.##',
      '..#.#.....',
      '##########',
      '#.######.#',
      '#.#####.##']

L2 = ['#.LL.L#.##',
      '#LLLLLL.L#',
      'L.L.L..L..',
      '#LLL.LL.L#',
      '#.LL.LL.LL',
      '#.LLLL#.##',
      '..L.L.....',
      '#LLLLLLLL#',
      '#.LLLLLL.L',
      '#.#LLLL.##']

L3 = ['#.##.L#.##',
      '#L###LL.L#',
      'L.#.#..#..',
      '#L##.##.L#',
      '#.##.LL.LL',
      '#.###L#.##',
      '..#.#.....',
      '#L######L#',
      '#.LL###L.L',
      '#.#L###.##']

L = L0.copy()
evolute(L, 1)
assert L == L1
evolute(L, 1)
assert L == L2
evolute(L, 1)
assert L == L3

# Sol input11.dat
#
# 2441
# 2190
#
# Time: 3.420 s
