from collections import defaultdict


with open("input") as f:
    distances = [line.strip().split(' ') for line in f.readlines()]


G = defaultdict(set)
for line in distances:
    a, _, b, _, d = line
    G[a].add((b, int(d)))
    G[b].add((a, int(d)))
vertices = set(G)


def extreme_hamiltonian(mode):
    def _extreme_hamiltonian(start, not_visited, mode):
        if len(not_visited) == 0:
            return 0
        return mode(w + _extreme_hamiltonian(e, not_visited - {e}, mode) for e, w in G[start] if e in not_visited)
    return mode(_extreme_hamiltonian(start, vertices - {start}, mode) for start in vertices)


# part I
print(extreme_hamiltonian(min))

# part II
print(extreme_hamiltonian(max))
