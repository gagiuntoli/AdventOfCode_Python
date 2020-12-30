import fileinput
import re

L = list([l.strip() for l in fileinput.input()])

def abba(w):
	for i in range(0, len(w) - 3):
		if w[i] == w[i+3] and w[i+1] == w[i+2] and w[i] != w[i+1]:
			return True
	return False

def aba(w):
	for i in range(0, len(w) - 2):
		if w[i] == w[i+2] and w[i] != w[i+1]:
			return True
	return False

def get_bab(w):
	bab = []
	for i in range(0, len(w) - 2):
		if w[i] == w[i+2] and w[i] != w[i+1]:
			bab.append(w[i+1]+w[i]+w[i+1])
	return bab

def search_aba(w, aba):
	for i in range(0, len(w) - 2):
		if w[i:i+3] == aba:
			return True
	return False

# Count ABBA

count = 0
for l in L:
	l = l.replace("[", " ")
	l = l.replace(']', " ")
	l = l.split()
	i = 0	
	a = 0
	valid = True
	for w in l:
		if i % 2 == 0:
			if abba(w):
				a += 1
		else:
			if abba(w):
				valid = False
				break
		i += 1
	if a > 0 and valid:
		count += 1
			
print(count)

# Count ABA

count = 0
for l in L:
	l = l.replace("[", " ")
	l = l.replace(']', " ")
	l = l.split()

	valid = False
	bab = []
	for k in range(0, len(l), 2):
		wa = get_bab(l[k])
		for i in wa:
			bab.append(i)

	for k in range(1, len(l), 2):
		for i in bab:
			if search_aba(l[k], i):
				valid = True
				break
	if valid:
		count += 1

print(count)
