import fileinput

L = list([l.strip() for l in fileinput.input()])

def con1(w):
	vocal = 0
	for l in w:
		if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
			vocal += 1
	if (vocal < 3):
		return False
	return True

def con2(w):
	for l in range(0, len(w) - 1):
		if w[l] == w[l+1]:
			return True
	return False

def con3(w):
	if w.find('ab') != -1:
		return False
	if w.find('cd') != -1:
		return False
	if w.find('pq') != -1:
		return False
	if w.find('xy') != -1:
		return False
	return True

def con4(w):
	for l in range(0, len(w) - 2):
		if w.find(w[l:l+2], l + 2, len(w)) != -1:
			return True
	return False

def con5(w):
	for l in range(0, len(w) - 2):
		if w[l] == w[l+2]:
			return True
	return False
	
		
count1 = 0
count2 = 0
for w in L:
	if con1(w) and con2(w) and con3(w):
		count1 += 1
	if con4(w) and con5(w):
		count2 += 1

print (count1)
print (count2)
