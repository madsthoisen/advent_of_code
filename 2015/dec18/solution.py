from copy import deepcopy

with open("input") as f:
    grid = [list(line.strip()) for line in f.readlines()]

inc = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]
h, w = len(grid), len(grid[0])

def neighbors_on(grid, r, c):
    add = 0
    for x, y in inc:
        if 0 <= r + x < h and 0 <= c + y < w: 
            if grid[r + x][c + y] == '#':
                add += 1
    return add 

def round(grid, part2=False):
    new_grid = deepcopy(grid)
    for i in range(h):
        for j in range(w):
            n = neighbors_on(grid, i, j)
            if grid[i][j] == '#' and n not in {2, 3}:
                new_grid[i][j] = '.'
            if grid[i][j] == '.' and n == 3:
                new_grid[i][j] = '#'
    if part2:
        new_grid[0][0] = new_grid[0][w - 1] = '#'
        new_grid[h - 1][0] = new_grid[h - 1][w - 1] = '#'
    return new_grid

# part I
grid_1 = deepcopy(grid)
for _ in range(100):
    grid_1 = round(grid_1)
print(sum(r.count('#') for r in grid_1))

# part II
grid[0][0] = grid[0][w - 1] = '#'
grid[h - 1][0] = grid[h - 1][w - 1] = '#'
for _ in range(100):
    grid = round(grid, part2=True)
print(sum(r.count('#') for r in grid))
