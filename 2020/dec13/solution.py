from functools import reduce
from math import inf

from sympy.ntheory.modular import solve_congruence

with open("input") as f:
    t, busses = [line.strip() for line in f.readlines()]
    t = int(t)
    busses = busses.split(',')

# part I
busses_active = [int(b) for b in busses if b.isdigit()]
m = inf
for bus in busses_active:
    wait = bus - t%bus
    if wait < m:
        m = wait
        bus_no = bus
print(bus_no * m)

# part II
a = [int(b) - i for i, b in enumerate(busses) if b.isdigit()]
print(solve_congruence(*list(zip(a, busses_active)))[0])
