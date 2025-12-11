import networkx as nx

from collections import defaultdict


with open("input") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]

G = nx.DiGraph()
G.add_edges_from((a, b) for a, bs in lines for b in bs.split(' '))

# part I
print(len(list(nx.all_simple_paths(G, 'you', 'out'))))

# part II
assert nx.is_directed_acyclic_graph(G)
tg = list(nx.topological_generations(G))
assert tg[0] == ['svr'] and tg[-1] == ['out']
dd = {(tg[0][0], 0): 1}
for bs in tg:
    new_dd = defaultdict(lambda: 0)
    for (a, n_visit), v in dd.items():
        for b in bs:
            if (a, b) in G.edges:
                new_dd[(b, n_visit + int(b in {'fft', 'dac'}))] += v
            else:
                new_dd[(a, n_visit)] = v
    dd = new_dd

print(dd[("out", 2)])
