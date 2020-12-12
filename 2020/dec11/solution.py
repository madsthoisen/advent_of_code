import itertools as it
import numpy as np

from copy import deepcopy

with open("input") as f:
    grid = [line.strip() for line in f.readlines()]

def get_adj(grid, i, j):
    h, w = len(grid), len(grid[0])
    adj = []
    dirs = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]
    for x, y in dirs:
        p_x, p_y = i + x, j + y
        if 0 <= p_x < h and 0 <= p_y < w:
            adj.append(grid[p_x][p_y])
    return adj

def get_seen(grid, i, j):
    h, w = len(grid), len(grid[0])
    seen = []
    dirs = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]
    for x, y in dirs:
        fac = 0
        while True:
            fac += 1
            p_x, p_y = i + fac * x, j + fac * y
            if 0 <= p_x < h and 0 <= p_y < w:
                p = grid[p_x][p_y]
                if p != '.':
                    seen.append(p)
                    break
            else:
                break
    return seen

def round(grid, consider, lim):
    h, w = len(grid), len(grid[0])
    new_grid = deepcopy(grid)
    for i in range(h):
        for j in range(w):
            pos = grid[i][j]
            if pos == '.':
                continue
            adj = consider(grid, i, j)
            if pos == '#' and adj.count('#') >= lim:
                new_grid[i] = new_grid[i][:j] + 'L' + new_grid[i][j + 1:]
            if pos == 'L' and '#' not in adj:
                new_grid[i] = new_grid[i][:j] + '#' + new_grid[i][j + 1:]
    return new_grid

def count_stb(grid, consider, lim):
    while True:
        old_grid = deepcopy(grid)
        grid = round(grid, consider, lim)
        if grid == old_grid:
            occ = sum(line.count('#') for line in grid)
            return occ

# part I
print(count_stb(grid, get_adj, 4))

# part II
print(count_stb(grid, get_seen, 5))
