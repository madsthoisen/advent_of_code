import numpy as np
import re


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

# part I
h, w = len(lines), len(lines[0])
stars = set()
nums = {}
add = 0
for y, line in enumerate(lines):
    stars |= {(j, y) for j, x in enumerate(line) if x == '*'}
    for m in re.finditer(r"\d+", line):
        a, b = m.start(0), m.end(0)
        nums[(a, b, y)] = int(m[0])
        r = range(a - 1, b + 1)
        surr = {(a - 1, y), (b, y)} | {(x, y - 1) for x in r} | {(x, y + 1) for x in r}
        if any(lines[y][x] != '.'for x, y in surr if 0 <= y < h and 0 <= x < w):
            add += nums[(a, b, y)]
print(add)

# part II
inc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
add = 0
for x, y in stars:
    gears = {val for i, j in inc for (a, b, yy), val in nums.items() if yy == y + j and a <= x + i < b}
    if len(gears) == 2:
        add += np.prod(list(gears))
print(add)
