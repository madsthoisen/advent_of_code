import numpy as np


with open("input") as f:
    ins = [line.strip().split(' ')[-4:] for line in f.readlines()]


def do(grid, i, part2=False):
    x1, y1, x2, y2 = map(int, i[1].split(',') + i[3].split(','))
    s = np.s_[y1:y2 + 1, x1:x2 + 1]
    if part2:
        grid[s] += 2 if i[0] == "toggle" else (1 if i[0] == "on" else -1)
        grid[s] = np.where(grid[s] > 0, grid[s], 0)
    else:
        grid[s] = (grid[s] + 1) % 2 if i[0] == "toggle" else (1 if i[0] == "on" else 0)
    return grid


def run(part2=False):
    grid = np.zeros([1000, 1000], dtype=int)
    [grid := do(grid, i, part2) for i in ins]
    return sum(sum(grid))


# part I
print(run())

# part II
print(run(True))
