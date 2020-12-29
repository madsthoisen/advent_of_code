import re

from collections import defaultdict

with open("input") as f:
    flips = [line.strip() for line in f.readlines()]

dirs = {'w': -2, 'e': 2, 'se': 1 - 0.5j,
        'ne': 1 + 0.5j, 'sw': -1 - 0.5j, 'nw': -1 + 0.5j}

def get_dir(pattern):
    d = 0
    while len(pattern) > 0:
        if pattern[0] in {'e', 'w'}:
            d += dirs[pattern[0]]
            pattern = pattern[1:]
            continue
        p = pattern[:2]
        pattern = pattern[2:]
        d += dirs[p]
    return d

def count_black_adj(tile, cols, dirs):
    return sum(1 for d in dirs.values() if cols[tile + d] == 1)

def get_neighbors(tile, dirs):
    return {tile - d for d in dirs.values()}

# part I
cols = defaultdict(int) 
for flip in flips:
    tile = get_dir(flip)
    cols[tile] = (cols[tile] + 1) % 2

print(list(cols.values()).count(1))

# part II
def day(cols):
    new_cols = cols.copy()
    check = set()
    for col in cols:
        check.add(col)
        check = check.union(get_neighbors(col, dirs))
    for col in check:
        b = count_black_adj(col, cols, dirs)
        if cols[col] == 0 and b == 2:
            new_cols[col] = 1
        elif cols[col] == 1 and (b == 0 or b > 2):
            new_cols[col] = 0 
    return new_cols


for _ in range(100):
    cols = day(cols)
print(list(cols.values()).count(1))
