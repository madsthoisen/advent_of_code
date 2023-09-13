from collections import defaultdict


with open("input") as f:
    distances = [line.strip().split(' ') for line in f.readlines()]


G = defaultdict(set)
for line in distances:
    a, _, b, _, d = line
    G[a].add((b, int(d)))
    G[b].add((a, int(d)))
vertices = set(G)


def extreme_hamiltonian(start, not_visited, mode):
    if len(not_visited) == 0:
        return 0
    return mode(w + extreme_hamiltonian(e, not_visited - {e}, mode) for e, w in G[start] if e in not_visited)


# part I
print(min(extreme_hamiltonian(start, vertices - {start}, min) for start in vertices))

# part II
print(max(extreme_hamiltonian(start, vertices - {start}, max) for start in vertices))
