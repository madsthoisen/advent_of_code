from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

north = {(i, -1) for i in [-1, 0, 1]}
south = {(i, 1) for i in [-1, 0, 1]}
west = {(-1, i) for i in [-1, 0, 1]}
east = {(1, i) for i in [-1, 0, 1]}
all_dirs = north | south | east | west

m = defaultdict(lambda: '.')
for y in range(len(lines)):
    for x in range(len(lines[0])):
        m[(x, y)] = lines[y][x]


def count_dirs(mm, x, y, dirs):
    return sum(mm[(x + i, y + j)] == '#' for i, j in dirs)


r = 0
while True:
    # proposals
    moves = {}
    count_moves = defaultdict(int)
    for (x, y), val in dict(m).items():
        if val == '.':
            continue
        tests = [(count_dirs(m, x, y, north), 0, -1),
                 (count_dirs(m, x, y, south), 0, 1),
                 (count_dirs(m, x, y, west), -1, 0),
                 (count_dirs(m, x, y, east), 1, 0)]
        for _ in range(r % 4):
            tests = tests[1:] + [tests[0]]
        if count_dirs(m, x, y, all_dirs) != 0:
            for c, ix, iy in tests:
                if c == 0:
                    moves[(x, y)] = (x + ix, y + iy)
                    count_moves[(x + ix, y + iy)] += 1
                    break
    # move
    n_moves = 0
    for (x, y), move in moves.items():
        if count_moves[move] < 2:
            m[(x, y)] = '.'
            m[move] = '#'
            n_moves += 1
    r += 1

    # part I
    if r == 10:
        mx = min(x for (x, y), val in m.items() if val == '#')
        Mx = max(x for (x, y), val in m.items() if val == '#')
        my = min(y for (x, y), val in m.items() if val == '#')
        My = max(y for (x, y), val in m.items() if val == '#')
        print(sum(m[(x, y)] == '.' for y in range(my, My + 1) for x in range(mx, Mx + 1)))

    # part II
    if n_moves == 0:
        print(r)
        break

