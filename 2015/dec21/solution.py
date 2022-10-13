import re

from itertools import combinations
from math import inf

with open("input") as f:
    boss = list(map(int, [re.search(r"\d+", l.strip())[0] for l in f.readlines()]))

with open("shop") as f:
    L = [b.split("\n") for b in f.read().split("\n\n")]

W, A, R = [[list(map(int, re.findall(r"\d+", line)))[-3:] for line in B[1:]] for B in L]
A += [[0, 0, 0]]
R = R[:-1] + [[0, 0, 0], [0, 0, 0]]

def fight(specs):
    a, d = 0, 1
    while specs[d][0] > 0:
        specs[d][0] -= specs[a][1] - specs[d][2]
        a, d = (a + 1) % 2, (d + 1) % 2
    return a

min_cost = inf
max_cost = 0
for w in W:
    for a in A:
        for r1, r2 in combinations(R, 2):
            me = [100, 0, 0] 
            me[1] += w[1] + a[1] + r1[1] + r2[1]
            me[2] += w[2] + a[2] + r1[2] + r2[2]
            cost = w[0] + a[0] + r1[0] + r2[0]
            res = fight([me, boss.copy()])
            if res == 0:
                min_cost = min(min_cost, cost)
            if res == 1:
                max_cost = max(max_cost, cost)

# part I
print(min_cost)

# part II
print(max_cost)
