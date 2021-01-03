import re

import matplotlib.pyplot as plt
import numpy as np

with open("input") as f:
    ins = [line.strip() for line in f.readlines()]


def change(grid, i):
    s = i.split(' ')
    if s[0] == "rect":
        c, r = list(map(int, s[1].split('x')))
        grid[0 : r, 0 : c] = 1
    elif s[0] == "rotate":
        cr, amnt = list(map(int, re.findall(r"\d+", i)))
        if s[1] == "column":
            grid[:, cr] = np.roll(grid[:, cr], amnt)
        if s[1] == "row":
            grid[cr, :] = np.roll(grid[cr, :], amnt)
    return grid

# part I
grid = np.zeros([6, 50], dtype=int)
for i in ins:
    grid = change(grid, i)
print(np.sum(grid))

# part II
plt.imshow(grid)
plt.show()
