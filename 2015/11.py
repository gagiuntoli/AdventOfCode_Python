import fileinput

def con1(word):
	for i in range(0, len(word) - 2):
		if ord(word[i]) + 1 == ord(word[i+1]) and ord(word[i]) + 2 == ord(word[i+2]):
			return True
	return False

def con2(word):
	if 'i' in word or 'o' in word or 'l' in word:
		return False
	return True

def con3(word):
	count = 0
	i = 0
	while i < len(word) - 1:
		if word[i] == word[i+1]: 
			count += 1;
			i += 2
		if count == 2:
			return True
		i += 1
	return False

def valid_password(word):
	return con1(word) and con2(word) and con3(word)

def increase_password(password):
	for i in range(len(password) - 1, 0, -1):
		l = list(password)
		if (l[i] == 'z'):
			l[i] = 'a'
			password = "".join(l)
		else:
			l[i] = chr(ord(l[i]) + 1)
			password = "".join(l)
			break
	return password
		
# Init

L = list([l.strip() for l in fileinput.input()])

password = L[0]

while True:
	if valid_password(password):
		break
	password = increase_password(password)

print(password)

password = increase_password(password)
while True:
	if valid_password(password):
		break
	password = increase_password(password)
print(password)

# Sol input11.dat
#
# hxbxxyzz
# hxcaabcc
#
# Time: 1.444 s
