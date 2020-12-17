from itertools import product
from operator import add

with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]

def evolve(dim, tmp, rounds):
    h, w = len(tmp), len(tmp[0])
    grid = {(x, y) + (0,) * (dim - 2): tmp[x][y] for x in range(h) for y in range(w)}
    inc = set(product([-1, 0, 1], repeat=dim)) - {(0,) * dim}

    def widen(grid):
        new_grid = {}
        for p in grid.keys():
            for i in inc:
                new_p = tuple(map(add, p, i))
                new_grid[new_p] = grid[new_p] if new_p in grid.keys() else '.'
        return new_grid

    def update(grid):
        new_grid = grid.copy()
        for p in grid.keys():
            n = [grid[tuple(map(add, p, i))] for i in inc if tuple(map(add, p, i)) in grid.keys()]
            new_grid[p] = '.' if grid[p] == '#' and n.count('#') not in [2, 3] else grid[p]
            new_grid[p] = '#' if grid[p] == '.' and n.count('#') == 3 else new_grid[p]
        return new_grid

    for _ in range(rounds):
        grid = widen(grid)
        grid = update(grid)

    return grid

# part I
print(list(evolve(3, tmp, 6).values()).count('#'))

# part II
print(list(evolve(4, tmp, 6).values()).count('#'))
