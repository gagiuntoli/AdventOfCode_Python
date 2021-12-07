import fileinput

L = [l.strip() for l in fileinput.input()]
positions = [int(x) for x in L[0].split(",")]
minH = min(positions)
maxH = max(positions)

minFuel = None
for H in range(minH, maxH+1):
	fuel = sum(abs(x - H) for x in positions)
	if H == minH or fuel < minFuel:
		minFuel = fuel

print(minFuel)

minFuel = None
for H in range(minH, maxH+1):
	fuel = sum(abs(x-H)*(abs(x-H)+1)//2 for x in positions)
	if H == minH or fuel < minFuel:
		minFuel = fuel

print(minFuel)

# Sol input .dat
#
# 355989
# 102245489
#
# Time: 0.443 s
