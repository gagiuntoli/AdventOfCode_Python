import fileinput

L = [list(l.strip()) for l in fileinput.input()]
W = len(L[0])
H = len(L)
for i in range(H):
	L[i] = [int(x) for x in L[i]]

def add_one(L):
	for i in range(H):
		for j in range(W):
			L[i][j] += 1

def search_and_flash(L):
	flashed = []
	for i in range(H):
		for j in range(W):
			flash(L,i,j,flashed)

def reset_flashed(L):
	count = 0
	for i in range(H):
		for j in range(W):
			if L[i][j] > 9:
				L[i][j] = 0
				count += 1
	return count

def flash(L,i,j,flashed=[]):
	if (i,j) in flashed:
		return
	adjacents = [(i+1,j-1),(i+1,j),(i+1,j+1),(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1),(i,j-1)]
	if L[i][j] > 9:
		flashed.append((i,j))
		for ip,jp in adjacents:
			if ip >= 0 and ip < H and jp >= 0 and jp < W:
				L[ip][jp] += 1
				flash(L,ip,jp,flashed)

count = 0
first_step = 0
for step in range(2000):
	add_one(L)
	search_and_flash(L)
	flashed = reset_flashed(L)
	if step < 100:
		count += flashed
	if flashed == H * W:
		first_step = step+1
		break

print(count)
print(first_step)

# Sol input11.dat
#
# 1649
# 256
#
# Time: 0.06 s
