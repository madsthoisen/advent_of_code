from collections import defaultdict
from itertools import count
from itertools import permutations


with open("input") as f:
    lines = f.read().split("\n")


freqs = defaultdict(list)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val != '.':
            freqs[val].append((r, c))


def get_antinodes(a, b, part):
    for i in [2] if part == 1 else count(1):
        p = (a[0] - i * (a[0] - b[0]), a[1] - i * (a[1] - b[1]))
        if 0 <= p[0] < len(lines) and 0 <= p[1] < len(lines[0]):
            yield p
        else:
            break


# part I
print(len({p for nodes in freqs.values() for a, b in permutations(nodes, 2) for p in get_antinodes(a, b, part=1)}))

# part II
print(len({p for nodes in freqs.values() for a, b in permutations(nodes, 2) for p in get_antinodes(a, b, part=2)}))
