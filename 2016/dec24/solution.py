import networkx as nx

from itertools import permutations


with open("input") as f:
    layout = [line.strip() for line in f.readlines()]


h, w = len(layout), len(layout[0])
numbers = {layout[i][j]: (i, j) for i in range(len(layout)) for j in range(len(layout[i])) if layout[i][j] not in {'.', '#'}}


G = nx.Graph()
for i in range(h - 1):
    for j in range(w - 1):
        if layout[i][j] != '#':
            if layout[i + 1][j] != '#':
                G.add_edge((i, j), (i + 1, j))
            if layout[i][j + 1] != '#':
                G.add_edge((i, j), (i, j + 1))

lengths = {(m, n): nx.shortest_path_length(G, source=numbers[m], target=numbers[n]) for m in numbers for n in numbers}

path_lengths = set()
path_lengths_reverse = set()
for p in permutations(numbers.keys(), len(numbers)):
    if p[0] == '0':
        path_length = sum(lengths[(p[i], p[i + 1])] for i in range(len(p) - 1))
        path_lengths.add(path_length)
        path_lengths_reverse.add(path_length + lengths[(p[-1], '0')])

# part I
print(min(path_lengths))


# part II
print(min(path_lengths_reverse))

