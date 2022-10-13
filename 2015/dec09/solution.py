from collections import defaultdict
from math import inf


with open("input") as f:
    distances = [line.strip() for line in f.readlines()]


G = defaultdict(set)
vertices = set()
for line in distances:
    a, _, b, _, d = line.split(' ')
    G[a].add((b, int(d)))
    G[b].add((a, int(d)))
    vertices = vertices.union({a, b})


def find_shortest_hamiltonian(start, v, G):
    if len(v) == 0:
        return 0
    m = inf
    for e, w in G[start]:
        if e in v:
            m = min(m, w + find_shortest_hamiltonian(e, v.difference({e}), G))
    return m

def find_longest_hamiltonian(start, v, G):
    if len(v) == 0:
        return 0
    m = 0
    for e, w in G[start]:
        if e in v:
            m = max(m, w + find_longest_hamiltonian(e, v.difference({e}), G))
    return m

# part I
print(min(find_shortest_hamiltonian(start, vertices.difference({start}), G) for start in vertices))

# part II
print(max(find_longest_hamiltonian(start, vertices.difference({start}), G) for start in vertices))
