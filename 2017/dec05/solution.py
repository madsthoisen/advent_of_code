from itertools import count

with open("input") as f:
	jumps_org = [int(x) for x in f.readlines()]


# part I
pos = 0
jumps = jumps_org[:]
for i in count(start=1):
	jump = jumps[pos]
	jumps[pos] += 1
	pos += jump
	if pos >= len(jumps):
		print(i)
		break


# part II
pos = 0
jumps = jumps_org[:]
for i in count(start=1):
	j = jumps[pos]
	if jumps[pos] >= 3:
		jumps[pos] -= 1
	else:
		jumps[pos] += 1
	pos += j
	if pos >= len(jumps):
		print(i)
		break
