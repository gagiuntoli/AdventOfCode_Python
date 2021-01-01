import fileinput

L = list([l.strip() for l in fileinput.input()])

P = {}
i = 0
for l in L:
	l = l.replace(':',' ')
	l = l.split()
	if l != []:
		if not i in P:
			P[i] = {}
		for j in range(0, len(l), 2):
			P[i][l[j]] = l[j+1]
	else:
		i += 1

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#    If cm, the number must be at least 150 and at most 193.
#    If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.

def con1():
	if P[p]['byr'].isnumeric() and len(P[p]['byr']) == 4:
		if 1920 <= int(P[p]['byr']) and int(P[p]['byr']) <= 2020:
			return True
	return False

def con2():
	if P[p]['iyr'].isnumeric() and len(P[p]['iyr']) == 4:
		if 2010 <= int(P[p]['iyr']) and int(P[p]['iyr']) <= 2020:
			return True
	return False

def con3():
	if P[p]['eyr'].isnumeric() and len(P[p]['eyr']) == 4:
		if 2020 <= int(P[p]['eyr']) and int(P[p]['eyr']) <= 2030:
			return True
	return False

def con4():
	f = P[p]['hgt']
	if f[len(f)-2:len(f)] == 'cm':
		if f[:len(f) - 2].isnumeric():
			if 150 <= int(f[:len(f) - 2]) and int(f[:len(f) - 2]) <= 193:
				return True
	elif f[len(f)-2:len(f)] == 'in':
		if f[:len(f)-2].isnumeric():
			if 59 <= int(f[:len(f)-2]) and int(f[:len(f)-2]) <= 76:
				return True
	return False

def con5():
	f = P[p]['hcl']
	if f[0] == '#' and len(f) == 7:
		return True
	return False

def con6():
	f = P[p]['ecl']
	if f == "amb" or f == "blu" or f == "brn" or f == "gry" or f == "grn" or f == "hzl" or f == "oth":
		return True
	return False

def con7():
	if P[p]['pid'].isnumeric() and len(P[p]['pid']) == 9:
		return True
	return False

count1 = 0
count2 = 0
for p in P:
	if 'byr' in P[p] and 'iyr' in P[p] and 'eyr' in P[p] and 'hgt' in P[p]:
		if 'hcl' in P[p] and 'ecl' in P[p] and 'pid' in P[p]:
			count1 += 1
			if con1() and con2() and con3() and con4() and con5():
				if con6() and con7():
					count2 += 1


print (count1)
print (count2)

# Sol input4.dat
#
# 245
# 133
#
# Time: 0.017 s
