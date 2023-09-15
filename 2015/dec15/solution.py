import re
import numpy as np


with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]
    ing = np.transpose(np.array([np.array(list(map(int, re.findall(r"-?\d+", x)))) for x in tmp]))


def score_and_calories(dist):
    v = ing * dist
    p = v[:-1].sum(axis=1)
    return np.prod(p[p > 0]), v[-1].sum()


dists = (np.array([i, j, k, 100 - i - j - k]) for i in range(101) for j in range(101 - i) for k in range(101 - i - j))
p1, p2 = 0, 0
for dist in dists:
    s, c = score_and_calories(dist)
    p1 = max(p1, s)
    if c == 500:
        p2 = max(p2, s)

# part I
print(p1)

# part II
print(p2)
