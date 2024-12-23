from collections import defaultdict


with open("input") as f:
    lines = [line.split('-') for line in f.read().split("\n")]


connections = defaultdict(set)
for a, b in lines:
    connections[a].add(b)
    connections[b].add(a)


def build(lim):
    groups = {(c,) for c in connections}
    for _ in range(lim):
        newgroups = set()
        for group in groups:
            for b in connections[group[0]]:
                if all(b in connections[x] for x in group[1:]):
                    newgroups.add(tuple(sorted(group + (b,))))
        if not newgroups:
            return groups
        groups = newgroups
    return groups


# part I
print(sum(a[0] == 't' or b[0] == 't' or c[0] == 't' for a, b, c in build(2)))

# part II
print(','.join(x for x in build(len(connections)).pop()))
