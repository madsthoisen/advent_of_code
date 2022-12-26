import re

from z3 import Int, Solver, If


with open("input") as f:
    lines = [map(int, re.findall("-?\d+", line)) for line in f.readlines()]

circles = [((sx, sy), abs(bx - sx) + abs(by - sy)) for sx, sy, bx, by in lines]


def manh(x, y):
    z3_abs = lambda x: If(x < 0, -x, x)
    return z3_abs(x[0] - y[0]) + z3_abs(x[1] - y[1])


fx, fy = Int("fx"), Int("fy")
s = Solver()
for (cx, cy), r in circles:
    s.add(manh((fx, fy), (cx, cy)) > r)
s.add(fx >= 0, fx <= 4000000)
s.add(fy >= 0, fy <= 4000000)
s.check()
fx = s.model()[fx].as_long()
fy = s.model()[fy].as_long()
print(4_000_000 * fx + fy)
