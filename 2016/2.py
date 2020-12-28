import fileinput

L = list([l.strip() for l in fileinput.input()])

def get_key(keypad, pos):
	key = ""
	for line in L:
		for i in line:
			if i == 'R' and pos[0] < len(keypad[0]) - 1:
				pos[0] += 1 if keypad[pos[1]][pos[0] + 1] != '0' else 0
			if i == 'L' and pos[0] > 0:
				pos[0] -= 1 if keypad[pos[1]][pos[0] - 1] != '0' else 0
			if i == 'D' and pos[1] < len(keypad) - 1:
				pos[1] += 1 if keypad[pos[1] + 1][pos[0]] != '0' else 0
			if i == 'U' and pos[1] > 0:
				pos[1] -= 1 if keypad[pos[1] - 1][pos[0]] != '0' else 0
		key += keypad[pos[1]][pos[0]]
	return key

keypad = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9']
]
pos = [1, 1]
key = get_key(keypad, pos)

print(key)

keypad = [
	['0', '0', '1', '0', '0'],
	['0', '2', '3', '4', '0'],
	['5', '6', '7', '8', '9'],
	['0', 'A', 'B', 'C', '0'],
	['0', '0', 'D', '0', '0']
]
pos = [0, 2]
key = get_key(keypad, pos)

print(key)
