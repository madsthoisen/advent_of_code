import numpy as np

from itertools import combinations


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


grid = np.array([np.array([1 if x == '#' else 0 for x in line]) for line in lines])
rows_no = set(i for i, x in enumerate(grid.sum(1)) if x == 0)
cols_no = set(i for i, x in enumerate(grid.sum(0)) if x == 0)


def manh(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(gap):
    add = 0
    for a, b in combinations(zip(*np.where(grid == 1)), 2):
        add_r = sum(gap for r in rows_no if min(a[0], b[0]) < r < max(a[0], b[0]))
        add_c = sum(gap for c in cols_no if min(a[1], b[1]) < c < max(a[1], b[1]))
        add += manh(a, b) + add_r + add_c
    return add


# part I
print(solve(1))

# part II
print(solve(999_999))
