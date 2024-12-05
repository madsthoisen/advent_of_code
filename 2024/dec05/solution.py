from collections import defaultdict
import functools


with open("input") as f:
    top, bottom = f.read().split("\n\n")


rules = defaultdict(list)
for line in top.split():
    a, b = map(int, line.split("|"))
    rules[a].append(b)

updates = [list(map(int, line.split(","))) for line in bottom.split()]

key_function = functools.cmp_to_key(lambda a, b: -(b in rules.get(a)))
part1, part2 = 0, 0
for upd in updates:
    upd_sorted = sorted(upd, key=key_function)
    m = len(upd) // 2
    if upd == upd_sorted:
        part1 += upd[m]
    else:
        part2 += upd_sorted[m]

# part I
print(part1)

# part II
print(part2)
