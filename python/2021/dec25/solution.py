from collections import defaultdict
from itertools import count


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


h, w = len(lines), len(lines[0])
fish = {(r, c): lines[r][c] for r in range(h) for c in range(w)}


def round(fish):
    new_fish = defaultdict(lambda: '.')
    for r, c in dict(fish):
        if fish[(r, c)] == '>':
            c_tmp = (c + 1) % w
            if fish[(r, c_tmp)] == '.':
                new_fish[(r, c_tmp)] = '>'
            else:
                new_fish[(r, c)] = '>'
        elif fish[(r, c)] == 'v':
            new_fish[(r, c)] = 'v'

    new_new_fish = defaultdict(lambda: '.')
    for r, c in dict(new_fish):
        if new_fish[(r, c)] == 'v':
            r_tmp = (r + 1) % h
            if new_fish[(r_tmp, c)] == '.':
                new_new_fish[(r_tmp, c)] = 'v'
            else:
                new_new_fish[(r, c)] = 'v'
        elif new_fish[(r, c)] == '>':
            new_new_fish[(r, c)] = '>'
    return new_new_fish


for i in count(1):
    old_fish = dict(fish)
    fish = round(fish)
    if fish == old_fish:
        print(i)
        break

