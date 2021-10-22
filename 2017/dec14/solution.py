import networkx as nx

from functools import reduce


with open("input") as f:
	key_string = f.read().strip()

def hex_to_binary(h):
	return bin(int(h, 16))[2:].zfill(4)

def knot_hash(input_str):
	lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
	numbers = list(range(256))
	pos, skip_size = 0, 0
	for _ in range(64):
		for length in lengths:
			tmp = []
			for i in range(length):
				tmp.append(numbers[(pos + i) % 256])
			tmp = tmp[::-1]
			for i in range(length):
				numbers[(pos + i) % 256] = tmp.pop(0)
			pos = (pos + length + skip_size) % 256
			skip_size += 1
	L = [reduce(lambda x, y: x ^ y, numbers[16 * i : 16 * i + 16]) for i in range(16)]
	hexadecimal_string = ''.join([hex(x)[2:].zfill(2) for x in L])
	return hexadecimal_string


grid = []
for row in range(128):
	row_str = ''.join([hex_to_binary(h) for h in knot_hash(key_string + '-' + str(row))])
	grid.append([int(x) for x in row_str])

# part I
print(sum([row.count(1) for row in grid]))

# part II
G = nx.Graph()
for row in range(128):
	for col in range(128):
		if grid[row][col] == 1:
			G.add_node((row, col))
			if row + 1 < 128 and grid[row + 1][col] == 1:
				G.add_edge((row, col), (row + 1, col))
			if col + 1 < 128 and grid[row][col + 1] == 1:
				G.add_edge((row, col), (row, col + 1))

print(len(list(nx.connected_components(G))))
