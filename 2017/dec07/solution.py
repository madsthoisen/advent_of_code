import matplotlib.pyplot as plt
import networkx as nx
import re

from collections import Counter, defaultdict


with open("input") as f:
	tmp = [line.split(" -> ") for line in f.readlines()]


weights = {}
G = nx.DiGraph()
for line in tmp:
	name, weight = line[0].split('(')
	weight = int(re.findall(r'\d+', weight)[0])
	name = name.strip()
	weights[name] = weight
	if len(line) > 1:
		children = [l.strip() for l in line[1].split(',')]
		for child in children:
			G.add_edge(name, child, weight=weight)

# part I
root = [n for n, d in G.in_degree() if d==0][0]
print(root)

# part II
def weight_subtree(tree, w=0):
	if G.degree(tree) == 0:
		return w + weights[tree]
	else:
		return weights[tree]  + sum(weight_subtree(t, w) for t in G[tree])

diff = 0
while True:
	weights_tmp = {tree: weight_subtree(tree) for tree in G[root]}
	one_out = Counter(weights_tmp.values()).most_common()[-1][0]
	new_diff = max(weights_tmp.values()) - min(weights_tmp.values())
	if new_diff == 0:
		print(weights[root] - diff)
		break
	root = list(weights_tmp.keys())[list(weights_tmp.values()).index(one_out)]
	diff = new_diff
	




