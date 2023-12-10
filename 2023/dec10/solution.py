import networkx as nx

from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line != "\n"]


connecting = {"|": ["n", "s"], "-": ["e", "w"], "L": ["n", "e"], "J": ["n", "w"], "7": ["s", "w"], "F": ["s", "e"]}
opposite = {"n": "s", "s": "n", "w": "e", "e": "w"}
going_in_dir = {d: [k for k, v in connecting.items() if d in v] + ["S"] for d in opposite}
details = {k: {x: going_in_dir[opposite[x]] for x in v} for k, v in connecting.items()}

G = nx.Graph()
d = {(r, c): x for r, ll in enumerate(lines) for c, x in enumerate(ll) if x != "."}
d = defaultdict(lambda: ".", d)
for (r, c), x in dict(d).items():
    if x == "S":
        start = (r, c)
        continue
    neighbors = {"n": (r - 1, c), "s": (r + 1, c), "w": (r, c - 1), "e": (r, c + 1)}
    for direction, neighbor in neighbors.items():
        if direction in details[x] and d[neighbor] in details[x][direction]:
            G.add_edge((r, c), neighbor)

loops = [list(p) for end in nx.neighbors(G, start) for p in nx.all_simple_paths(G, start, end)]
loop = next(l for l in loops if len(l) > 2)

# part I
print(len(loop) // 2)

# part II
rows, cols = len(lines), len(lines[0])
d = defaultdict(lambda: ".", {(r, c): "#" for r, c in loop})
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
edges = [
    ((r, c), (r + x, c + y))
    for r in range(rows)
    for c in range(cols)
    for x, y in dirs
    if d[(r, c)] == d[(r + x, c + y)] == "."
]
G = nx.Graph()
G.add_edges_from(edges)
cc = defaultdict(set, {p: c for c in nx.connected_components(G) for p in c})


old_r, old_c = loop[0]
inside = set()
for r, c in loop[1:]:
    if c != old_c:
        inc = 1 if c > old_c else -1
        for col in [old_c, c]:
            b = (r - inc, col)
            if d[b] == ".":
                inside |= cc[b] | {b}
    if r != old_r:
        inc = 1 if r > old_r else -1
        for row in [r, old_r]:
            b = (row, c + inc)
            if d[b] == ".":
                inside |= cc[b] | {b}
    old_r, old_c = r, c

print(len(inside))
