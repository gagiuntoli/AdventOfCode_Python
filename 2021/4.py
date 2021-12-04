import fileinput

L = [l.strip() for l in fileinput.input()]

numbers = L[0].split(",")
bingos = []

line_num = 2
while line_num < len(L):
	line_count = 0
	bingo = []
	while line_count < 5:
		bingo.append(L[line_num+line_count].split())
		line_count += 1
	line_num += 6
	bingos.append(bingo)

def mark_bingo(bingos, bingos_check, num):
	for b,bingo in enumerate(bingos):
		for i in range(5):
			for j in range(5):
				if bingo[i][j] == num:
					bingos_check[b][i][j] = 1
	
def check_bingo_by_id(bingos_check, b):
	bingo = bingos_check[b]
	for i in range(5):
		is_bingo = True
		for j in range(5):
			if bingo[i][j] == 0:
				is_bingo = False
				break
		if is_bingo:
			return b
	for j in range(5):
		is_bingo = True
		for i in range(5):
			if bingo[i][j] == 0:
				is_bingo = False
				break
		if is_bingo:
			return b
	return -1

bingos_check = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(bingos))]

for num in numbers:
	mark_bingo(bingos, bingos_check, num)
	found = False
	for b in range(len(bingos)):
		if check_bingo_by_id(bingos_check, b) != -1:
			suma = 0
			for i in range(5):
				for j in range(5):
					if bingos_check[b][i][j] == 0:
						suma += int(bingos[b][i][j])
			found = True
			break
	if found:
		break

print(suma * int(num))

bingos_check = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(bingos))]

W = {}
winners_count = 0
for num in numbers:
	mark_bingo(bingos, bingos_check, num)
	found = False
	for b in range(len(bingos)):
		if check_bingo_by_id(bingos_check, b) != -1 and b not in W.keys():
			W[b] = True
			winners_count += 1
		if winners_count == len(bingos):
			suma = 0
			for i in range(5):
				for j in range(5):
					if bingos_check[b][i][j] == 0:
						suma += int(bingos[b][i][j])
			found = True
			break
	if found:
		break

print(suma * int(num))

# Sol input .dat
#
# 71708
# 34726
#
# Time: 0.093 s
