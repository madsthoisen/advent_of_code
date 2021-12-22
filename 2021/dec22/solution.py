import re

from shapely.geometry import box
from tqdm import tqdm
from collections import defaultdict


with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


def get(lines, cap=False):
    pols = defaultdict(lambda: box(0, 0, 0, 0))
    for mode, points in tqdm(lines):
        x0, x1, y0, y1, z0, z1 = map(int, re.findall("-?\d+", points))
        b = box(x0, y0, x1 + 1, y1 + 1)
        if cap:
            if x0 < -50 or x1 > 50 or y0 < -50 or y1 > 50 or z0 < -50 or z1 > 50:
            continue
        for z in range(z0, z1 + 1):
            pols[z] = pols[z].union(b) if mode == 'on' else pols[z].difference(b)
    return sum(int(p.area) for p in pols.values())


# part I
print(get(lines, True))

# part II
print(get(lines))
