import numpy as np

from collections import defaultdict

with open("input") as f:
	map_tmp = [line.strip() for line in f.readlines()]


h, w = len(map_tmp), len(map_tmp[0])
map_ = defaultdict(lambda:'.')
for i in range(h):
	for j in range(w):
		map_[(i, j)] = map_tmp[i][j]

general_change_rules = {'u': {'r': 'r', 'l': 'l', 'rev': 'd', 'none': 'u'},
						'r': {'r': 'd', 'l': 'u', 'rev': 'l', 'none': 'r'},
						'd': {'r': 'l', 'l': 'r', 'rev': 'u', 'none': 'd'},
						'l': {'r': 'u', 'l': 'd', 'rev': 'r', 'none': 'l'}
						}

direction_to_move = {'u': np.array([-1, 0]),
					 'r': np.array([0, 1]),
					 'd': np.array([1, 0]),
					 'l': np.array([0, -1])}

def burst(map_, pos, face):
	node = map_[(pos[0], pos[1])]
	face = general_change_rules[face][type_to_direction[node]]
	map_[(pos[0], pos[1])] = change_dic[node]
	inf = (map_[(pos[0], pos[1])] == '#')
	pos += direction_to_move[face]
	return map_, pos, face, inf

# part I
change_dic = {'#': '.', '.': '#'}
type_to_direction = {'.': 'l', '#': 'r'}
count = 0
face = 'u'
pos = np.array([h // 2, w // 2])
map_part_1 = map_.copy()
for _ in range(10000):
	map_part_1, pos, face, inf = burst(map_part_1, pos, face)
	count += inf

print(count)

# part II
change_dic = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}
type_to_direction = {'.': 'l', 'W': 'none', '#': 'r', 'F': 'rev'}

count = 0
face = 'u'
pos = np.array([h // 2, w // 2])
map_part_1 = map_.copy()
for _ in range(10_000_000):
	map_part_1, pos, face, inf = burst(map_part_1, pos, face)
	count += inf

print(count)
