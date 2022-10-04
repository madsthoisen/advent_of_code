import numpy as np

from itertools import combinations

with open("input") as f:
    tmp = sorted(list(map(int, f.readlines())), reverse=True)


def f(group_weight):
    r = 2
    while True:
        acc = {el for el in combinations(tmp, r) if sum(el) == group_weight}
        if len(acc) > 0:
           return acc 
        r += 1

# part I
ent = {np.product(a) for a in f(sum(tmp) // 3)}
print(min(ent))

# part II
ent = {np.product(a) for a in f(sum(tmp) // 4)}
print(min(ent))

