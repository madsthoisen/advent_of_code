from collections import defaultdict


with open("input") as f:
    m = [line.strip() for line in f.readlines()]

h, w = len(m), len(m[0])
grid = defaultdict(lambda: '.', {(r, c): m[r][c] for r in range(h) for c in range(w)})


def check(r, c, gg):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(gg[(r + dr, c + dc)] == '@' for dr, dc in dirs) < 4


# part I
print(sum(check(r, c, grid) for r in range(h) for c in range(w) if grid[(r, c)] == '@'))

# part II
rem = 0
while True:
    old_rem = rem
    for (r, c), val in grid.items():
        if val == '@' and check(r, c, grid):
            grid[(r, c)] = '.'
            rem += 1
    if old_rem == rem:
        print(rem)
        break
