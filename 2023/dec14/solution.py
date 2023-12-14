import numpy as np

from itertools import count


def tilt(grid):
    for r in range(rows):
        for c in range(cols):
            x = grid[r, c]
            if x == 'O':
                for rr in range(1, r + 1):
                    above = grid[r - rr, c]
                    if above == '.':
                        grid[r - rr, c] = 'O'
                        grid[r - rr + 1, c] = '.'
                    else:
                        break
    return grid


def cycle(g):
    for _ in range(4):
        g = tilt(g)
        g = np.rot90(g, axes=(1, 0))
    return g


def load(grid):
    return sum(rows - r for r in range(rows) for c in range(cols) if grid[(r, c)] == 'O')


with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line != "\n"]

grid = np.array([np.array(list(line)) for line in lines])
rows, cols = len(lines), len(lines[0])

# part I
print(load(tilt(grid)))

# part II
goal = 1_000_000_000
table = {}
stop = False
for i in count(1):
    grid = cycle(grid)
    hash = grid.tobytes()
    if hash in table and not stop:
        cycle_len = i - table[hash]
        stop = (goal - i) % cycle_len + i
    table[hash] = i
    if i == stop:
        print(load(grid))
        break
