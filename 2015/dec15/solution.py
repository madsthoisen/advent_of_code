import re

import numpy as np

with open("input") as f:
    tmp = [l.strip().split(": ") for l in f.readlines()]
    specs = np.array(list(np.array(list(map(int, re.findall(r"\-?\d+", v)))) for k, v
            in tmp))
    cals = specs[:, -1]
    specs = np.matrix(specs).transpose()[:-1, :]


def score(use):
    totals = np.matmul(specs, use.transpose())
    return np.prod(totals[totals > 0])


combs = (np.array([i, j, k, 100 - i - j - k]) for i in range(101)
                                              for j in range(101 - i)
                                              for k in range(101 - i - j))

M, M_cal = 0, 0
for use in combs:
    s = score(use)
    M = max(M, s)
    if np.dot(use, cals) == 500:
        M_cal = max(M_cal, s)

# part I
print(M)

# part II
print(M_cal)
