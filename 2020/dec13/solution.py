import numpy as np

from functools import reduce
from math import inf
from sympy.ntheory.modular import solve_congruence

with open("input") as f:
    t, busses = [line.strip() for line in f.readlines()]
    t = int(t)
    busses = busses.split(',')

# part I
busses_active = [int(b) for b in busses if b.isdigit()]
W = np.array([[bus, bus - t % bus] for bus in busses_active])
earliest = np.argmin(W, 0)[1]
print(np.prod(W[earliest]))

# part II // Chinese Remainder Theorem
a = [int(b) - i for i, b in enumerate(busses) if b.isdigit()]
print(solve_congruence(*list(zip(a, busses_active)))[0])
