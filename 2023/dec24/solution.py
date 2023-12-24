import numpy as np
import re

from z3 import Int, Solver


with open("input") as f:
    stones = [list(map(int, re.findall(r"-?\d+", line))) for line in f.readlines()]


# part I
low, high = 200000000000000, 400000000000000
add = 0
for i in range(len(stones)):
    px1, py1, pz1, vx1, vy1, vz1 = stones[i]
    for j in range(i + 1, len(stones)):
        px2, py2, pz2, vx2, vy2, vz2 = stones[j]
        A = np.array([[vx1, -vx2], [vy1, - vy2]])
        b = np.array([px2 - px1, py2 - py1])
        try:
            s, t = np.linalg.solve(A, b)
            x = px1 + s * vx1
            y = py1 + s * vy1
            if s >= 0 and t >= 0 and low <= x <= high and low <= y <= high:
                add += 1
        except np.linalg.LinAlgError:
            pass
print(add)

# part II
s = Solver()
a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
s.add(a >= 0)
s.add(b >= 0)
s.add(c >= 0)
for i, (px, py, pz, vx, vy, vz) in enumerate(stones):
    tmp_s = Int(f"s_{i}")
    s.add(tmp_s >= 0)
    s.add(tmp_s <= 2000000000000)

    tmp_t = Int(f"s_{i}")
    s.add(tmp_t >= 0)
    s.add(tmp_t <= 2000000000000)

    s.add(px + vx * tmp_s == a + d * tmp_t)
    s.add(py + vy * tmp_s == b + e * tmp_t)
    s.add(pz + vz * tmp_s == c + f * tmp_t)

s.check()
m = s.model()
print(m[a].as_long() + m[b].as_long() + m[c].as_long())
