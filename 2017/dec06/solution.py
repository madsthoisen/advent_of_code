import numpy as np

from itertools import count


with open("input") as f:
	banks = [int(x) for x in f.read().split("\t")]


# part I and II
seen = {tuple(banks): 0}
l = len(banks)
for c in count(start=1):
	idx = np.argmax(banks)
	val = banks[idx]
	banks[idx] = 0
	for i in range(val):
		banks[(idx + i + 1) % l] += 1
	if (t := tuple(banks)) in seen:
		print(c) # part I
		print(c - seen[t]) # part II
		break
	seen[t] = c
