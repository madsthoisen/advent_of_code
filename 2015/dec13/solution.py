import networkx as nx
from collections import defaultdict

with open("input") as f:
    tmp = [line.strip()[:-1].split(' ') for line in f.readlines()]

def get_increase(path, G):
    return sum([G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)]) + G[path[len(path) - 1]][path[0]]["weight"]

gains = defaultdict(int)
for L in tmp:
    gains[tuple(sorted([L[0], L[-1]]))] += int(L[3]) if L[2] == "gain" else -int(L[3])

# part I
G = nx.Graph()
G.add_weighted_edges_from([key + (val,) for key, val in gains.items()])

print(max([get_increase(path, G) for s in G for t in G for path in nx.all_simple_paths(G, s, t) if len(path) == len(G)]))

# part II
G.add_weighted_edges_from([("Me", guest, 0) for guest in G])
print(max([get_increase(path, G) for s in G for t in G for path in nx.all_simple_paths(G, s, t) if len(path) == len(G)]))
