import networkx as nx

from math import dist

with open("input") as f:
    pos = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

ll = len(pos)
distances = {(i, j): dist(pos[i], pos[j]) for i in range(ll - 1) for j in range(i + 1, ll)}
distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

G = nx.Graph()
for count, (i, j) in enumerate(distances):
    if count == 1000:
        comps = sorted([len(comp) for comp in nx.connected_components(G)], reverse=True)
        print("part I", comps[0] * comps[1] * comps[2])
    G.add_edge(i, j)
    if len(list(nx.connected_components(G))[0]) == ll:
        print("part II", pos[i][0] * pos[j][0])
        break
