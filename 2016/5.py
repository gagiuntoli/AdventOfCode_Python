
# Hashing 

import fileinput
import hashlib

L = list([l.strip() for l in fileinput.input()])

ivalue = L[0]

password = ""
number = 0
for i in range(8):
	hashed = hashlib.md5((ivalue+str(number)).encode()).hexdigest()
	while hashed[0:5] != '00000':
		number += 1
		hashed = hashlib.md5((ivalue+str(number)).encode()).hexdigest()
	password += hashed[5]
	number += 1

print (password)

def filled(password):
	for i in password:
		if i == None:
			return False
	return True

password2 = [ None ] * 8 
number = 0
while not filled(password2):
	hashed = hashlib.md5((ivalue+str(number)).encode()).hexdigest()
	while hashed[0:5] != '00000':
		number += 1
		hashed = hashlib.md5((ivalue+str(number)).encode()).hexdigest()
	if hashed[5].isdigit(): 
		if int(hashed[5]) >= 0 and int(hashed[5]) < 8:
			if password2[int(hashed[5])] == None:
				password2[int(hashed[5])] = hashed[6]
	number += 1

password = ""
for i in password2:
	password += i

print (password)
