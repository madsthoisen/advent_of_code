from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


grid = {}
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        pos = -r * 1j + c
        if val == '^':
            start = pos
            val = '.'
        grid[pos] = val


def run(grid, pos, extra=None):
    d = 1j
    seen = defaultdict(set, {pos: {d}})
    while True:
        npos = pos + d
        val = grid.get(npos, "O")
        if val == '#' or npos == extra:
            d *= -1j
            continue
        elif val == 'O':
            return seen
        elif npos in seen and d in seen[npos]:
            return True
        else:
            seen[npos].add(d)
            pos = npos


# part I
seen = run(grid, start)
print(len(seen))


# part II
print(sum(run(grid, start, extra=pos) is True for pos in seen if pos != start))
