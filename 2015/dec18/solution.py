import numpy as np


with open("input") as f:
    lights = np.array([np.array([int(x == '#') for x in line.strip()]) for line in f.readlines()])


def step(lights, part2=False):
    fixed = lights.copy()
    for r in range(h):
        for c in range(w):
            if part2 and r in {0, h - 1} and c in {0, w - 1}:
                continue
            s = fixed[max(r - 1, 0): min(r + 2, h + 1), max(c - 1, 0): min(c + 2, w + 1)].sum()
            if fixed[r, c] and s not in {3, 4}:
                lights[r, c] = 0
            elif not fixed[r, c] and s == 3:
                lights[r, c] = 1
    return lights


w, h = lights.shape

# part I
l_tmp = lights.copy()
[l_tmp := step(l_tmp) for _ in range(100)]
print(l_tmp.sum())

# part II
lights[0, h - 1] = lights[0, 0] = lights[w - 1, 0] = lights[w - 1, h - 1] = 1
[lights := step(lights, True) for _ in range(100)]
print(lights.sum())
