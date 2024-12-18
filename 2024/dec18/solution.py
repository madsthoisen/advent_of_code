import networkx as nx


with open("input") as f:
    corrupted = [tuple(map(int, line.split(','))) for line in f.read().split("\n")]


G = nx.Graph()
for r in range(71):
    for c in range(71):
        if (r, c) in corrupted[:1024]:
            continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in corrupted[:1024]:
                G.add_edge((r, c), (nr, nc))


# part I
print(nx.shortest_path_length(G, (0, 0), (70, 70)))

# part II
corrupted = corrupted[1024:]
while True:
    rr, rc = corrupted.pop(0)
    G.remove_node((rr, rc))
    if not nx.has_path(G, (0, 0), (70, 70)):
        print(f"{rr},{rc}")
        break
