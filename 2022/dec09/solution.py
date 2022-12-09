import numpy as np
from numpy import sign
from numpy.linalg import norm


with open("input") as f:
    lines = [line.strip().split() for line in f.readlines()]


k = [np.zeros(2) for _ in range(10)]
p1 = {tuple(k[1])}
p2 = {tuple(k[9])}
moves = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}
for move, b in lines:
    for _ in range(int(b)):
        k[0] += moves[move]
        for i in range(1, 10):
            h, t = k[i - 1: i + 1]
            d = h - t
            if norm(d, 2) == 2 or norm(d, 1) > 2:
                t[0] += sign(d[0])
                t[1] += sign(d[1])
            p1.add(tuple(k[1]))
            p2.add(tuple(k[9]))

# part I
print(len(p1))

# part II
print(len(p2))