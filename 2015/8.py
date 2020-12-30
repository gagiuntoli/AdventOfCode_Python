import fileinput

def real_length(word):
	length = 0
	i = 1	
	while i < len(word) - 1:
		if word[i] == '\\' and word[i+1] == '"':
			i += 2
		elif word[i] == '\\' and word[i+1] == '\\':
			i += 2
		elif word[i] == '\\' and word[i+1] == 'x':
			i += 4
		else:
			i += 1
		length += 1
	return length


def encode_length(word):
	length = 2

	for i in word:
		if i == '\\' or i == '"':
			length += 2
		else:
			length += 1
	return length


L = list([l.strip() for l in fileinput.input()])

length_1 = 0
length_2 = 0
length_3 = 0

for l in L:
	length_1 += len(l)
	length_2 += real_length(l)
	length_3 += encode_length(l)

print(length_1 - length_2)
print(length_3 - length_1)

# Sol input8.dat
#
# 1342
# 2074
#
# Time: 0.029 s
