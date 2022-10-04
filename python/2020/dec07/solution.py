import numpy as np
import networkx as nx
import re

with open("input") as f:
    tmp = [re.split(",|contains?", re.sub("bags?", "", line).strip()) for line in f.readlines()]
    rules = [[l.replace(".","").strip() for l in line] for line in tmp]

root = "shiny gold"

G = nx.DiGraph()
for rule in rules:
    node = rule[0]
    neighbors = rule[1:]
    if neighbors[0] == "no other":
        continue
    for n in neighbors:
        _, num, col = re.split("(\d+ )", n)
        G.add_edge(node, col, weight=int(num))

# Part I
print(sum(nx.has_path(G,node, root) for node in G.nodes()) - 1)

# Part II
def path_weight_prod(p):
    return np.prod([G[p[i]][p[i+1]]["weight"] for i in range(len(p) - 1)])

paths = [p for node in G for p in nx.simple_paths.all_simple_paths(G, root, node)]
print(sum(path_weight_prod(path) for path in paths))


