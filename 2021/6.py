import fileinput

L = [l.strip() for l in fileinput.input()]
fish_days = [int(x) for x in L[0].split(",")]

def fish_after(days):
	F = [0 for _ in range(9)]
	for day in fish_days:
		F[day] += 1

	for day in range(days):
		with_zero_days = F[0]
		for i in range(8):
			F[i] = F[i+1]
		F[6] += with_zero_days
		F[8] = with_zero_days

	return sum(F)
			
print(fish_after(80))
print(fish_after(256))

# Sol input .dat
#
# 343441
# 1569108373832
#
# Time: 0.041 s
