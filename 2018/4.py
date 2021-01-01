import fileinput
import datetime

L = list([l.strip() for l in fileinput.input()])

data = []
for l in L:
	time_str = l[1:17]
	time_obj = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')
	l = l.split()
	g = int(l[3][1:]) if l[2] == 'Guard' else -1
	data.append([time_obj, g])

S = {}
data.sort() # Sort by dates
i = 0
while i < len(data):
	if data[i][1] != -1:
		g = data[i][1]
		i += 1
	else:
		start = data[i][0].minute
		end = data[i+1][0].minute
		if not g in S:
			S[g] = [end- start, [0] * 60]
		else:
			S[g][0] += end - start
			for t in range(start, end):
				S[g][1][t] += 1
		i += 2

# Part 1

max_s = -1000000
for s in S:
	if S[s][0] > max_s:
		max_s = S[s][0]
		max_g = s

max_minute = -1000000
for i, j in enumerate(S[max_g][1]):
	if j > max_minute:
		max_minute = j
		minute = i

print(minute * max_g)

# Part 1

M = {}
for s in S:
	max_minute = -1000000
	for i, j in enumerate(S[s][1]):
		if j > max_minute:
			max_minute = j
			minute = i
	M[s] = [minute, max_minute]

max_minute = -1000000
for s in M:
	if M[s][1] > max_minute:
		max_minute = M[s][1]
		minute = M[s][0]
		max_g = s
print(minute * max_g)
	
# Sol input4.dat
#
# 143415
# 49944
#
# Time: 0.026 s
