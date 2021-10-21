import networkx as nx


with open("input") as f:
	pipes = [line.strip().split(' <-> ') for line in f.readlines()]


G = nx.Graph()
for pipe in pipes:
	for val in pipe[1].split(', '):
		G.add_edge(pipe[0], val)

# part I
print([len(c) for c in nx.connected_components(G) if '0' in c][0])

# part II
print(len(list(nx.connected_components(G))))
