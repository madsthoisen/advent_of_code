import networkx as nx
from functools import reduce


with open("input") as f:
    lines = [list(map(int, line.strip())) for line in f.readlines()]


G = nx.Graph()
h, w = len(lines), len(lines[0])
dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
risk = 0
for y in range(h):
    for x in range(w):
        height = lines[y][x]
        low_point = True
        for i, j in dirs:
            x_tmp, y_tmp = x + i, y + j
            if 0 <= x_tmp < w and 0 <= y_tmp < h:
                if (tmp_height := lines[y_tmp][x_tmp]) <= height:
                    low_point = False
                elif tmp_height != 9:
                    G.add_edge((x_tmp, y_tmp), (x, y))
        if low_point:
            risk += (height + 1)

# part I
print(risk)

# part II
component_lengths = sorted([len(c) for c in nx.connected_components(G)], reverse=True)
print(reduce(lambda x, y: x * y, component_lengths[:3], 1))
