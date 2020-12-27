import fileinput

L = list([l.strip() for l in fileinput.input()])

mov = list(L[0])
x = 0
y = 0
hauses = {(x,y)}
for m in mov:
	if m == '>':
		 x += 1
	if m == '<':
		 x -= 1
	if m == '^':
		 y += 1
	if m == 'v':
		 y -= 1
	hauses.add((x,y))

print (len(hauses))

x1 = 0
y1 = 0
hauses1 = {(x1,y1)}
x2 = 0
y2 = 0
hauses2 = {(x2,y2)}
for i, m in enumerate(mov):
	if (i % 2):
		if m == '>':
			 x1 += 1
		if m == '<':
			 x1 -= 1
		if m == '^':
			 y1 += 1
		if m == 'v':
			 y1 -= 1
		hauses1.add((x1,y1))
	else:
		if m == '>':
			 x2 += 1
		if m == '<':
			 x2 -= 1
		if m == '^':
			 y2 += 1
		if m == 'v':
			 y2 -= 1
		hauses2.add((x2,y2))

print(len(hauses1.union(hauses2)))
