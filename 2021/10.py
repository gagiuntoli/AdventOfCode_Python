import fileinput

L = [l.strip() for l in fileinput.input()]

P1 = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
P2 = { ")": 1, "]": 2, "}": 3, ">": 4 }
INV = { "(": ")", "[": "]", "{": "}", "<": ">" }

def find_score_stack(stack):
	score = 0
	for i in range(len(stack)-1, -1, -1):
		score *= 5
		if stack[i] in INV.keys():
			score += P2[INV[stack[i]]]
	return score
	
def check_error(line):
	stack = []
	for w in line:
		if w in INV.keys():
			stack.append(w)
		elif len(stack) > 0:
			val = stack.pop()
			if INV[val] != w:
				return "Corrupted", w
	return "Incomplete", find_score_stack(stack)

score_corrupted = 0
scores_incomplete = []
for line in L:
	line_error, value = check_error(line)
	if line_error == "Corrupted":
		score_corrupted += P1[value]
	else:
		scores_incomplete.append(value)	

scores_incomplete.sort()
print(score_corrupted)
print(scores_incomplete[len(scores_incomplete)//2])

# Sol input10.dat
#
# 362271
# 1698395182
#
# Time: 0.036 s
