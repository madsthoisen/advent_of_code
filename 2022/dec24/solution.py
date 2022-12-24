from itertools import count


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


def run(blizzards, occ, start, goal):
    positions = {start}
    for minute in count(1):

        # move blizzards
        occ = set()
        for i, (x, y, d) in enumerate(blizzards):
            nx, ny = x + dirs[d][0], y + dirs[d][1]

            nx = 1 if nx > w - 2 else nx
            ny = 1 if ny > h - 2 else ny
            nx = w - 2 if nx <= 0 else nx
            ny = h - 2 if ny <= 0 else ny

            blizzards[i] = (nx, ny, d)
            occ.add((nx, ny))

        # move you
        new_positions = set()
        for x, y in positions:
            for i, j in list(dirs.values()) + [(0, 0)]:
                xi, yj = x + i, y + j
                if (xi, yj) == goal:
                    return minute, blizzards, occ
                elif (xi, yj) in m and m[(xi, yj)] != '#' and (xi, yj) not in occ:
                    new_positions.add((xi, yj))
        positions = new_positions


dirs = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
h, w = len(lines), len(lines[0])
m = {(x, y): lines[y][x] for y in range(h) for x in range(w)}
blizzards = [(x, y, v) for (x, y), v in m.items() if v in dirs]
occ = {(x, y) for x, y, _ in blizzards}

add = 0
start, end = (1, 0), (w - 2, h - 1)
for i, (s, g) in enumerate([(start, end), (end, start), (start, end)]):
    res, blizzards, occ = run(blizzards, occ, s, g)
    if i == 0:
        print(res)  # part I
    add += res

# part II
print(add)
