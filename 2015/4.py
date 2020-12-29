
# Hashing

import fileinput
import hashlib

L = list([l.strip() for l in fileinput.input()])

ivalue = L[0]

number = 0
while hashlib.md5((ivalue+str(number)).encode()).hexdigest()[0:5] != '00000':
	number += 1

print (number)

number = 0
while hashlib.md5((ivalue+str(number)).encode()).hexdigest()[0:6] != '000000':
	number += 1

print (number)
