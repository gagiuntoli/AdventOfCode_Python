import fileinput
from itertools import permutations

L = list([l.strip() for l in fileinput.input()])

def calc_distance(cities, distances):
	dist = 0
	for i in range(0, len(cities) - 1):
		if (cities[i], cities[i+1]) in distances:
			dist += distances[(cities[i], cities[i+1])]
		elif (cities[i+1], cities[i]) in distances:
			dist += distances[(cities[i+1], cities[i])]
		else:
			print ("distance from ", cities[i], " to ", cities[i+i], "not found")
			return -1
	return dist

distances = {}
cities = set()

for l in L:
	l = l.split()
	cities.add(l[0])
	cities.add(l[2])
	distances[(l[0], l[2])] = int(l[4])

min_dist = 1000000000
for cities_p in permutations(cities):
	dist = calc_distance(cities_p, distances)
	if (dist < min_dist):
		min_dist = dist

max_dist = -1000000000
for cities_p in permutations(cities):
	dist = calc_distance(cities_p, distances)
	if (dist > max_dist):
		max_dist = dist

print (min_dist)
print (max_dist)

# Sol input9.dat
#
# 207
# 804
#
# Time: 0.204 s
