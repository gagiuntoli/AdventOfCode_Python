import fileinput

L = [l.strip() for l in fileinput.input()][0].split()
xmin = int(L[2].split("=")[1].split("..")[0])
xmax = int(L[2].split("=")[1].split("..")[1][:-1])
ymin = int(L[3].split("=")[1].split("..")[0])
ymax = int(L[3].split("=")[1].split("..")[1])
box = [xmin,xmax,ymin,ymax]

def is_in_box(box,p):
	[xmin,xmax,ymin,ymax] = box
	if xmin <= p[0] and p[0] <= xmax and ymin <= p[1] and p[1] <= ymax:
		return True
	return False

def check_intersep(v,box,max_ts):
	p = [0,0]
	ymax = p[1]
	for t in range(max_ts):
		p[0] += v[0]
		p[1] += v[1]
		if v[0] > 0:
			v[0] -= 1
		elif v[0] < 0:
			v[0] += 1
		v[1] -= 1
		ymax = max(ymax,p[1])
		if is_in_box(box,p):
			return ymax
	return None

max_ts = 500
min_vx = -200
min_vy = -200
max_vx = 300
max_vy = 300

V = {}
ymax = -100000
for vx in range(min_vx, max_vx):
	for vy in range(min_vy, max_vy):
		v = [vx, vy]
		ymax_t = check_intersep(v[:],box,max_ts)
		if ymax_t != None:
			ymax = max(ymax,ymax_t)
			V[(v[0],v[1])] = True

print(ymax)
print(len(V.keys()))

# Sol input17.dat
#
# 4278
# 1994
#
# Time: 50.2 s
