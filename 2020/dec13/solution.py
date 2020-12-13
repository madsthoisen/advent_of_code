from functools import reduce
from math import inf

with open("input") as f:
    t, busses = [line.strip() for line in f.readlines()]
    t = int(t)
    busses = busses.split(',')

## https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

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
print(chinese_remainder(busses_active, a))
