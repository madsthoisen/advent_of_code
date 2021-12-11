import numpy as np

from itertools import count


with open("input") as f:
    _energy = np.array([np.array(list(map(int, line.strip()))) for line in f.readlines()])


def step(energy):
    flashed = set()
    energy += 1
    while energy.max() > 9:
        for r, c in np.argwhere(energy > 9):
            flashed.add((r, c))
            energy[max(r - 1, 0) : r + 2, max(c - 1, 0) : c + 2] += 1
        for r, c in flashed:
            energy[r][c] = 0
    return len(flashed)


# part I
energy = np.array(_energy)
print(sum(step(energy) for _ in range(100)))

# part II
energy = np.array(_energy)
print(next(s for s in count(1) if step(energy) == np.prod(energy.shape)))
