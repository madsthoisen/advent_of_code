from collections import defaultdict
from itertools import product

with open("input") as f:
    containers = list(map(int, f.readlines()))

m = defaultdict(int)
add = 0
for vec in product(range(2), repeat=len(containers)):
    tmp = [containers[i] for i, val in enumerate(vec) if val == 1]
    if sum(tmp) == 150:
        add += 1
        m[sum(vec)] += 1

# part I
print(add)

# part II
print(m[min(m.keys())])

