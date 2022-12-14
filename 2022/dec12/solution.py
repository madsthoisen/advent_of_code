import networkx as nx


with open("input") as f:
    lines = [list(line.strip()) for line in f.readlines()]


w, h = len(lines[0]), len(lines)
G = nx.DiGraph()
starts = set()
for y in range(h):
    for x in range(w):
        pos = lines[y][x]
        if pos == 'S':
            S = (y, x)
            pos = 'a'
        elif pos == 'E':
            E = (y, x)
            pos = 'z'
        if pos == 'a':
            starts.add((y, x))
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xi, yj = x + i, y + j
            if 0 <= xi < w and 0 <= yj < h:
                new = lines[yj][xi]
                if new == 'S':
                    new = 'a'
                elif new == 'E':
                    new = 'z'
                if ord(new) - ord(pos) <= 1:
                    G.add_edge((y, x), (yj, xi))
# part I
print(len(nx.shortest_path(G, S, E)) - 1)

# part II
print(min(len(nx.shortest_path(G, s, E)) - 1 for s in starts if nx.has_path(G, s, E)))
