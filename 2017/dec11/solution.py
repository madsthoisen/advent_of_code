import numpy as np


with open("input") as f:
	directions = f.read().strip().split(',')


def shortest_path(p):
	return int(abs(pos.real) + (abs(pos.imag) - abs(pos.real)) / 2)


translate = {'n': 2j,
			 's': -2j,
			 'ne': 1 + 1j,
			 'nw': -1 + 1j,
			 'se': 1 - 1j,
			 'sw': -1 -1j}
m = 0
pos = 0
for d in directions:
	pos += translate[d]
	m = max(m, shortest_path(pos))

# part I
print(shortest_path(pos))

#part II
print(m)
