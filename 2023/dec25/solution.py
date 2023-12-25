import networkx as nx


with open("input") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]


G = nx.Graph()
edges = [(a, b) for a, ll in lines for b in ll.split()]
G.add_edges_from(edges)
cut = nx.minimum_edge_cut(G)
G.remove_edges_from(cut)
a, b = nx.connected_components(G)
print(len(a) * len(b))
