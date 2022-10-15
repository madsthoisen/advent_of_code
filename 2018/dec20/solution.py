import networkx as nx


with open("input") as f:
    regex = f.read().strip()[1:-1]


dirs = {'W': (-1, 0), 'E': (1, 0), 'N': (0, 1), 'S': (0, -1)}
def parse_regex(regex, org):
    x, y = org
    while regex:
        char, regex = regex[0], regex[1:]
        if char in dirs:
            i, j = dirs[char]
            new = (x + i, y + j)
            G.add_edge((x, y), new)
            x, y = new
        elif char == '|':
            x, y = org
        elif char == '(':
            (x, y), regex = parse_regex(regex, new)
        elif char == ')':
            return org, regex

def get_depth(G, source):
    depth = 0
    layer = [source]
    visited = set()
    while layer:
        depth += 1
        next_layer = []
        for node in layer:
            for child in G[node]:
                if child not in visited:
                    next_layer.append(child)
                    visited.add(child)
        layer = next_layer
    return depth - 1

G = nx.Graph()
p = (0, 0)
parse_regex(regex, p)

# part I
print(get_depth(G, p))

# part II
print(sum(1 for l in nx.shortest_path_length(G, p).values() if l >= 1000))
