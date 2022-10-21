import numpy as np
import re

from itertools import count
from math import inf, gcd


with open("input") as f:
    pos = np.array([np.array(list(map(int, re.findall(r"-?\d+", line)))) for line in f.readlines()])


def lcm(arr):
    out = 1
    for x in arr:
        out = out * x // gcd(x, out)
    return out

def v_up(v, p):
    for i, a in enumerate(p):
        for j in range(i + 1, 4):
            b = p[j]
            v[i] -= a > b
            v[i] += a < b
            v[j] -= b > a
            v[j] += b < a
    return v

def energy(pos, vels):
    e = lambda arr: sum(abs(x) for x in arr)
    return sum(e(px) * e(vx) for px, vx in zip(pos, vels))


vels = np.array([np.zeros(3, dtype=int) for _ in range(4)])
cycles = [inf for _ in range(3)]
start = np.array([np.array(arr) for arr in pos])
for i in count(1):
    vels = v_up(vels, pos)
    pos += vels
    if all(pos[:, 0] == start[:, 0]) and all(vels[:, 0] == 0):
        cycles[0] = min(i, cycles[0])
    if all(pos[:, 1] == start[:, 1]) and all(vels[:, 1] == 0):
        cycles[1] = min(i, cycles[1])
    if all(pos[:, 2] == start[:, 2]) and all(vels[:, 2] == 0):
        cycles[2] = min(i, cycles[2])
    if all(x < inf for x in cycles):
        print("part 2:", lcm(cycles))
        break
    if i == 1000:
        print("part 1:", energy(pos, vels))

