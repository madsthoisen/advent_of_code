import string

from collections import defaultdict
from itertools import count
from itertools import combinations


with open("input") as f:
    lines = f.read().split("\n")


freqs = defaultdict(list)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val in set(string.ascii_letters) | {str(x) for x in range(10)}:
            freqs[val].append((r, c))


def get_antinodes(a, b, part):
    iterator = [2] if part == 1 else count(1)
    dx, dy = a[0] - b[0], a[1] - b[1]
    out = set()
    for i in iterator:
        a1 = (a[0] - i * dx, a[1] - i * dy)
        a2 = (b[0] + i * dx, b[1] + i * dy)
        a1_inside = (0 <= a1[0] < len(lines) and 0 <= a1[1] < len(lines[0]))
        a2_inside = (0 <= a2[0] < len(lines) and 0 <= a2[1] < len(lines[0]))
        if a1_inside:
            out.add(a1)
        if a2_inside:
            out.add(a2)
        if not a1_inside and not a2_inside:
            break
    return out


# part I
print(len({p for nodes in freqs.values() for a, b in combinations(nodes, 2) for p in get_antinodes(a, b, part=1)}))

# part II
print(len({p for nodes in freqs.values() for a, b in combinations(nodes, 2) for p in get_antinodes(a, b, part=2)}))
