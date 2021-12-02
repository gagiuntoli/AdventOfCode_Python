import fileinput

L = list([l.strip() for l in fileinput.input()])

h = 0
depth = 0
for line in L:
	line = line.split()
	inst = line[0]
	amount = int(line[1])
	if inst == "forward":
		h += amount
	elif inst == "up":
		depth -= amount
	elif inst == "down":
		depth += amount

print(h * depth)

h = 0
depth = 0
aim = 0
for line in L:
	line = line.split()
	inst = line[0]
	amount = int(line[1])
	if inst == "forward":
		h += amount
		depth += aim * amount
	elif inst == "up":
		aim -= amount
	elif inst == "down":
		aim += amount

print(h * depth)


# Sol input1.dat
#
# 2039256
# 1856459736
#
# Time: 0.041 s
