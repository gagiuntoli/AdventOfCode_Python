import fileinput
from itertools import permutations  

L = list([l.strip() for l in fileinput.input()])

nums = []
for l in L[0]:
	nums.append(int(l))

width = 25
height = 6

def count_layer(nums, index, width, height):
	zeros = 0
	ones = 0
	twos = 0
	for i in range(width * height):
		if nums[index + i] == 0:
			zeros += 1
		if nums[index + i] == 1:
			ones += 1
		if nums[index + i] == 2:
			twos += 1
	return zeros, ones, twos
	
	
layer_num = len(nums) // (width * height)

minzeros = 100000000
for i in range(layer_num):
	zeros, ones, twos = count_layer(nums, i * width * height, width, height)
	if zeros < minzeros:
		minzeros = zeros 
		minones = ones
		mintwos = twos

print(minones * mintwos)

for h in range(height):
	image = ""
	for w in range(width):
		for l in range(layer_num):
			pixel = nums[h * width + w + l * (width * height)]
			if pixel != 2:
				image += str(pixel) if pixel == 1 else " "
				break
	print(image)
		
# Sol input8.dat
#
# 1320
# RCYKR
#
# Time: 0.022 s
