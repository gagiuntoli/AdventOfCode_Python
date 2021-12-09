import fileinput

M = [list(l.strip()) for l in fileinput.input()]

H = len(M)
W = len(M[0])

def get_valid_points(i, j):
	points = []
	if i > 0:
		points.append((i-1,j))
	if j > 0:
		points.append((i,j-1))
	if i < H-1:
		points.append((i+1,j))
	if j < W-1:
		points.append((i,j+1))
	return points

def adjacent_are_lower(i,j):
	for ip, jp in get_valid_points(i,j):
		if M[ip][jp] <= M[i][j]:
			return False
	return True

def basin_size(i,j, visited=[]):
	if M[i][j] == "9" or (i,j) in visited:
		return 0
	else:
		visited.append((i,j))
	res = 1
	for ip, jp in get_valid_points(i,j):
		res += basin_size(ip,jp, visited)	
	return res

count = 0
basis = []
for i in range(H):
	for j in range(W):
		if adjacent_are_lower(i,j):
			count += int(M[i][j]) + 1
			basis.append(basin_size(i,j))
basis.sort()

print(count)
print(basis[-1]*basis[-2]*basis[-3])

# Sol input9.dat
#
# 560
# 959136
#
# Time: 1.13 s Ein Jahr Zusammen :)
