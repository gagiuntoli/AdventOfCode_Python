#
# Transverse Graph
#
# Solution based on the one given by "0xdf"
# https://0xdf.gitlab.io/adventofcode2019/6
#

import fileinput
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])

def count_orbits(ORB, start, count):
	counta = 0
	for o in ORB[start]:
		counta += count_orbits(ORB, o, count + 1) 
	return count + counta

def find_path(ORB, prev, start, end, dist):
	if start == end:
		return dist
	for o in ORB[start]:
		if not o in prev:
			distn = find_path(ORB, prev + [o], o, end, dist + 1)
			if distn >= 0:
				return distn
	return -1


ORB = defaultdict(list)
ORB2 = defaultdict(list)
for l in L:
	l = l.split(')')
	ORB[l[0]].append(l[1])
	ORB2[l[0]].append(l[1])
	ORB2[l[1]].append(l[0])

print (count_orbits(ORB, 'COM', 0))
print (find_path(ORB2, ['YOU'], 'YOU', 'SAN', 0) - 2)

# Sol input6.dat
#
# 621125
# 550
#
# Time: 0.037 s
