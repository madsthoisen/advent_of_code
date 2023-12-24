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
px_s, py_s, pz_s = Int("px_s"), Int("py_s"), Int("pz_s")
vx_s, vy_s, vz_s = Int("vx_s"), Int("vy_s"), Int("vz_s")
s.add(px_s >= 0)
s.add(py_s >= 0)
s.add(pz_s >= 0)
for i, (px, py, pz, vx, vy, vz) in enumerate(stones):
    t = Int(f"t_{i}")
    s.add(t >= 0)
    s.add(t <= 2000000000000)

    s.add(px + vx * t == px_s + vx_s * t)
    s.add(py + vy * t == py_s + vy_s * t)
    s.add(pz + vz * t == pz_s + vz_s * t)

s.check()
m = s.model()
print(m[px_s].as_long() + m[py_s].as_long() + m[pz_s].as_long())
