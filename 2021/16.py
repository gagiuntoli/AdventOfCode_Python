import fileinput
import binascii
from functools import reduce

def calc(T, ops):
	if T == 0:
		return sum(ops)
	elif T == 1:
		return reduce((lambda x, y: x * y), ops)
	elif T == 2:
		return min(ops)
	elif T == 3:
		return max(ops)
	elif T == 5:
		return 1 if ops[0] > ops[1] else 0
	elif T == 6:
		return 1 if ops[0] < ops[1] else 0
	elif T == 7:
		return 1 if ops[0] == ops[1] else 0
	else:
		print("Error:", T, ops)

def get_packet(packet, versions):

	V = int(packet[0:3],2)
	T = int(packet[3:6],2)
	versions.append(V)
	if T == 4:
		num_s = ""
		j = 6
		while True:
			num_s += packet[j+1:j+5]	
			if packet[j] == '0':
				break
			j+=5
		num = int(num_s,2)
		return j+5, num
	else:
		I = packet[6]
		if I == '0':
			L = int(packet[7:22],2)
			bits = 0
			ops = []
			while bits < L:
				b, res = get_packet(packet[bits+22:], versions)
				ops.append(res)
				bits += b
			return 22+bits, calc(T, ops)
		else:
			L = int(packet[7:18],2)
			bits = 0
			ops = []
			for i in range(L): 
				b, res = get_packet(packet[bits+18:], versions)
				ops.append(res)
				bits += b
			return 18+bits, calc(T, ops)

hex_string = [l.strip() for l in fileinput.input()][0]

bits = len(hex_string) * 4
integer = int(hex_string, 16)
bin_string = format(integer, '0>'+str(bits)+'b')

versions = []
packet, res = get_packet(bin_string, versions)

print(sum(versions))
print(res)

# Sol input16.dat
#
# 873
# 402817863665
#
# Time: 0.05 s
