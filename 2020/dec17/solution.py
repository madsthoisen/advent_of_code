import numpy as np

from collections import defaultdict
from itertools import product

with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]

def evolve(dim, tmp, rounds):
    h, w = len(tmp), len(tmp[0])
    grid = {(x, y) + (0,) * (dim - 2): tmp[x][y] for x in range(h) for y in range(w)}

    def widen(grid):
        new_grid = grid.copy()
        for p in grid.keys():
            for i in product([-1, 0, 1], repeat=dim):
                if i != (0,) * dim:
                    new_p = tuple([e1 + e2 for e1, e2 in zip(p, i)])
                    if new_p not in grid.keys():
                        new_grid[new_p] = '.'
        return new_grid

    def update(grid):
        new_grid = grid.copy()
        for p in grid.keys():
            n = []
            for i in product([-1, 0, 1], repeat=dim):
                if i == (0,) * dim:
                    continue
                new_p = tuple([e1 + e2 for e1, e2 in zip(p, i)])
                if new_p in grid.keys():
                    n.append(grid[new_p])
            if grid[p] == '#':
                if n.count('#') not in [2, 3]:
                    new_grid[p] = '.'
            else:
                if n.count('#') == 3:
                    new_grid[p] = '#'
        return new_grid


    for _ in range(rounds):
        grid = widen(grid)
        grid = update(grid)
    return grid

# part I
print(list(evolve(3, tmp, 6).values()).count('#'))

# part II
print(list(evolve(4, tmp, 6).values()).count('#'))
