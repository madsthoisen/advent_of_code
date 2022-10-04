from itertools import product
from operator import add

with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]

def evolve(dim, tmp, rounds):
    h, w = len(tmp), len(tmp[0])
    grid = {(x, y) + (0,) * (dim - 2): tmp[x][y] for x in range(h) for y in range(w)}
    inc = set(product([-1, 0, 1], repeat=dim)) - {(0,) * dim}

    def update(grid):
        extension = {new_p: '.' for p in grid.keys() for i in inc if (new_p := tuple(map(add, p, i))) not in grid.keys()}
        grid = {**grid, **extension}
        new_grid = grid.copy()
        for p in grid.keys():
            n = [grid[new_p] for i in inc if (new_p := tuple(map(add, p, i))) in grid.keys()]
            new_grid[p] = '.' if grid[p] == '#' and n.count('#') not in [2, 3] else grid[p]
            new_grid[p] = '#' if grid[p] == '.' and n.count('#') == 3 else new_grid[p]
        return new_grid

    for _ in range(rounds):
        grid = update(grid)

    return grid

# part I
print(list(evolve(3, tmp, 6).values()).count('#'))

# part II
print(list(evolve(4, tmp, 6).values()).count('#'))
