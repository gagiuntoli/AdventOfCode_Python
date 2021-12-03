import fileinput

L = [l.strip() for l in fileinput.input()]

def get_ones_amount_for_bit(L, bit):
	
	if bit >= len(L[0]):
		return None
	ones = 0

	for line in L:
		ones += 1 if line[bit] == "1" else 0
	return ones


num_bits = len(L[0])
num_values = len(L)
ones_gamma = [0 for _ in range(num_bits)]

for line in L:
	for j,c in enumerate(line):
		ones_gamma[j] += 1 if c == "1" else 0
gamma = ""
epsilon = ""
for val in ones_gamma:
	if val > num_values // 2:
		gamma += "1"
		epsilon += "0"
	else:
		gamma += "0"
		epsilon += "1"

print(int(gamma,2) * int(epsilon,2))

old_list = L.copy()
bit = 0
while bit < num_bits:

	if len(old_list) == 1:
		new_list = old_list.copy()
		break

	new_list = []
	ones_amount_bit = get_ones_amount_for_bit(old_list, bit)
	for line in old_list:
		if ones_amount_bit > len(old_list) // 2 or ones_amount_bit * 2 == len(old_list): 
			if line[bit] == "1":
				new_list.append(line)
		else:
			if line[bit] == "0":
				new_list.append(line)
	old_list = new_list.copy()
	bit += 1

rating_1 = new_list[0]

old_list = L.copy()
bit = 0
while bit < num_bits:

	if len(old_list) == 1:
		new_list = old_list.copy()
		break

	new_list = []
	ones_amount_bit = get_ones_amount_for_bit(old_list, bit)
	for line in old_list:
		if ones_amount_bit > len(old_list) // 2 or ones_amount_bit * 2 == len(old_list): 
			if line[bit] == "0":
				new_list.append(line)
		else:
			if line[bit] == "1":
				new_list.append(line)
	old_list = new_list.copy()
	bit += 1

rating_2 = new_list[0]

print(int(rating_1,2) * int(rating_2,2))


# Sol input3.dat
#
# 3901196
# 4412188
#
# Time: 0.045 s
