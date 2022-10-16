import networkx as nx


with open("input") as f:
    orbits = [line.strip().split(')') for line in f.readlines()]


G = nx.Graph()
G.add_edges_from(orbits)
    
# part I
print(sum(nx.shortest_path_length(G, node, 'COM') for node in G.nodes))

# part II
print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2)
