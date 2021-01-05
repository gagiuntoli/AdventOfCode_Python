import fileinput

L = list([l.strip() for l in fileinput.input()])

def decode(w):
	w = w.replace("F", "0")
	w = w.replace("B", "1")
	w = w.replace("R", "1")
	w = w.replace("L", "0")
	return int(w, 2)
	
ids = []
for l in L:
	ids.append(decode(l))

print(max(ids))

ids.sort()
for i in range(0, len(ids) - 1):
	if ids[i]+2 == ids[i+1]:
		myid = ids[i]+1

print(myid)

# Sol input5.dat
#
# 919
# 642
#
# Time: 0.017 s
