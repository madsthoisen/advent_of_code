import networkx as nx

from math import inf


with open("input") as f:
    lines = f.read().split("\n")


h, w = len(lines), len(lines[0])
G = nx.DiGraph()
DIRS = {1j: (-1, 0), -1j: (1, 0), 1: (0, 1), -1: (0, -1)}
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        z = c - r * 1j
        if val == "S":
            start = (z, 1)
        if val == "E":
            e = z
        if val != "#":
            for d, (dr, dc) in DIRS.items():
                if 0 <= r + dr < h and 0 <= c + dc < w and lines[r + dr][c + dc] != "#":
                    G.add_edge((z, d), (z + d, d), weight=1)
            for d in DIRS:
                G.add_edge((z, d), (z, d * 1j), weight=1000)
                G.add_edge((z, d), (z, d * (-1j)), weight=1000)

shortest = inf
for d in DIRS:
    if (e, d) in G.nodes:
        length = nx.shortest_path_length(G, start, (e, d), weight="weight")
        if length < shortest:
            shortest = length
            shortest_paths = nx.all_shortest_paths(G, start, (e, d), weight="weight")
            seen = {p[0] for path in shortest_paths for p in path}

# part I
print(shortest)

# part II
print(len(seen))
