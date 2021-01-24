import fileinput
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])

D = defaultdict(list)
DS = defaultdict(list)

for l in L:
	l = l.replace('.','')
	l = l.split("bags contain")
	a = l[0].replace(' ','')
	for i in l[1].split(","):
		if not "no other" in i:
			i = i[1:].split(" ")
			n = int(i[0])
			D[a].append((n,i[1]+i[2]))
			DS[a].append(i[1]+i[2])

all_bags = set()
for i in DS:
	all_bags.add(i)	
	for j in DS[i]:
		all_bags.add(j)	

def how_many_contain(bag_target):
	count = 0
	for b in all_bags:
		if contain(b, bag_target): count += 1
	return count

def contain(bag_search, bag_target):
	
	if bag_target in DS[bag_search]:
		return True
	for i in DS[bag_search]:
		if contain(i, bag_target):
			return True
	return False

def how_many(bag_target):
	count = 0
	for i in D[bag_target]:
		count += i[0] * 1 if D[i[1]] == [] else i[0] + i[0] * how_many(i[1])
	return count



print(how_many_contain("shinygold"))
print(how_many("shinygold"))

# Sol input7.dat
#
# 261
# 3765
#
# Time: 0.028 s
