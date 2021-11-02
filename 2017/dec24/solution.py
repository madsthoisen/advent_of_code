with open("input") as f:
    components = [tuple(sorted(list(map(int, line.strip().split('/'))))) for line in f.readlines()]

bridges = [(c, [x for x in components if x != c]) for c in components if c[0] == 0]
best = 0
longest = 0
longest_bridges = []
while bridges:
    new_bridges = []
    while bridges:
        bridge, remaining = bridges.pop()
        for a, b in remaining:
            new_remaining = [x for x in remaining if x != (a, b)]
            if bridge[-1] == a:
                new_bridges.append((bridge + (a, b), new_remaining))
            if bridge[-1] == b:
                new_bridges.append((bridge + (b, a), new_remaining))
        if (weight := sum(bridge)) > best:
            best = weight
        if (l := len(bridge)) > longest:
            longest_bridges = []
            longest = l
        if l == longest:
            longest_bridges.append(bridge)
    bridges = new_bridges

# part I
print(best)

# part II
print(max(sum(bridge) for bridge in longest_bridges))


