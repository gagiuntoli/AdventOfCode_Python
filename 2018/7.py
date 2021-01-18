# Solution based on:
# https://0xdf.gitlab.io/adventofcode2018/#day-7
#

import fileinput
from collections import defaultdict
import copy

L = list([l.strip() for l in fileinput.input()])


block_by = defaultdict(list)
for l in L:
	l = l.split()
	block_by[l[7]].append(l[1])


def solve(block_by, num_workers, base_time):

	all_steps = set([x for y in block_by for x in block_by[y]] + [x for x in block_by])
	available_steps = [x for x in all_steps if x not in block_by]
	workers = [('',-1) for x in range(0, num_workers)]
	steps_done = []
	steps_in_execution = []

	t = 0
	
	while True:

		# Finish available tasks
		for w in workers:
			if t == w[1]:
				if not w[0] in steps_done:
					steps_done.append(w[0])
				for x in block_by:
					if w[0] in block_by[x]:
						block_by[x].remove(w[0])
				delete = [x for x in block_by if block_by[x] == []]
				for x in delete: del block_by[x] 
				steps_in_execution.remove(w[0])

		if len(steps_done) == len(all_steps):
			break

		# Assign new tasks
		available_steps = [x for x in all_steps \
				   	if x not in block_by and \
					   x not in steps_done and \
					   x not in steps_in_execution]
		available_steps.sort()
		for wi, w in enumerate(workers):
			if len(available_steps) == 0:
				break
			if t >= w[1]:
				step = available_steps.pop(0)
				workers[wi] = (step, t + ord(step) - ord('A') + base_time + 1)
				steps_in_execution.append(step)
		t += 1

	sol = ""
	for s in steps_done:
		sol += s
	
	return sol, t
				
	
print(solve(copy.deepcopy(block_by), 1, 0)[0])
print(solve(copy.deepcopy(block_by), 5, 60)[1])
	
# Sol input7.dat
#
# BFLNGIRUSJXEHKQPVTYOCZDWMA
# 880
#
# Time: 0.055 s
