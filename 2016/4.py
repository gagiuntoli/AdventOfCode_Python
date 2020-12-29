
# Checksums and Caesar Cipher

import fileinput
import re
import collections

L = list([l.strip() for l in fileinput.input()])


def valid_word(word, checksum):
	
	W = collections.Counter(word)

	min_rep = 0
	for j in range(0, len(checksum) - 1):
		a = 0
		b = 0
		if checksum[j] in W.keys():
			a = W[checksum[j]]
		if checksum[j+1] in W.keys():
			b = W[checksum[j+1]]
		if a < b:
			return False
		min_rep = b

	for k in W.keys():
		if not k in checksum:
			if W[k] > min_rep:
				return False
	return True


def caesar_cipher(word, n):

	result = ""
	for i in range(0, len(word)):
		if word[i] == '-':
			result += " "
		else:
			result += chr((ord(word[i]) - 97 + n) % 26 + 97)
	return result


id_object = 0
count = 0

for l in L:

	# Extract checksum
	x = re.findall("\[.*\]", l)
	checksum = x[0][1:len(x[0])-1]

	# Extract ID
	x = re.findall("\d+", l)
	num = int(x[0])

	# Extract Text
	x = re.findall("[a-z\-]+", l)
	decripted = caesar_cipher(x[0], num)
	if "northpole" in decripted:
		id_object = num
	word = x[0].replace("-", "")
	if valid_word(word, checksum):
		count += num

print (count)
print (id_object)
