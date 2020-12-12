import numpy as np

with open ("input") as f:
    grid = [line.strip() for line in f.readlines()]

def move(pos, r, d, grid):
    return (pos[0] + d, (pos[1] + r) % len(grid[0]))

def el(grid, pos):
    return grid[pos[0]][pos[1]]

def count(slope, grid):
    pos = (0,0)
    count = 0
    while True:
        count += (el(grid, pos) == '#')
        pos = move(pos, slope[0], slope[1], grid)
        if pos[0] >= len(grid):
            return count

# part 1
print(count((3, 1), grid))

# part 2
directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(np.prod(list(map(lambda d: count(d, grid), directions))))

