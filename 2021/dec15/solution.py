import networkx as nx
import numpy as np

from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra


with open("input") as f:
    lines = np.array([np.array(list(map(int, line.strip()))) for line in f.readlines()])


def get_least_weight_path(lines):
    G = nx.DiGraph()
    h, w = len(lines), len(lines[0])
    for y in range(h):
        for x in range(w):
            if y + 1 < h:
                G.add_edge((y, x), (y + 1, x), weight = lines[y + 1][x])
                G.add_edge((y + 1, x), (y, x), weight = lines[y][x])
            if x + 1 < w:
                G.add_edge((y, x), (y, x + 1), weight = lines[y][x + 1])
                G.add_edge((y, x + 1), (y, x), weight = lines[y][x])
    return single_source_dijkstra(G,(0, 0), (h - 1, w - 1))[0]


# part I
print(get_least_weight_path(lines))

# part II
def inc(arr, n):
    for _ in range(n):
        arr = arr + 1
        arr[arr > 9] = 1
    return arr

lines = np.vstack([np.hstack([inc(lines, i + j) for j in range(5)]) for i in range(5)])
print(get_least_weight_path(lines))
