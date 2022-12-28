import re

from itertools import count


with open("input") as f:
    lines = f.readlines()


clay = set()
min_y, max_y = 999999999, 0
for line in lines:
    a, b, c = map(int, re.findall("\d+", line))
    for i in range(b, c + 1):
        (x, y) = (a, i) if line[0] == 'x' else (i, a)
        clay.add((x, y))
        min_y, max_y = min(min_y, y), max(max_y, y)


flowing = set()
still = set()
springs = {(500, 0)}
springs_seen = set()
while springs:
    x, y = springs.pop()
    springs_seen.add((x, y))

    while (x, y) not in still.union(clay) and y <= max_y:
        flowing.add((x, y))
        y += 1

    if y > max_y:
        continue

    y -= 1

    while True:
        dirs = {-1: False, 1: False}
        borders = {-1: None, 1: None}
        for d in [-1, 1]:
            for j in count(0):
                if (x + d * j, y) in clay:
                    dirs[d] = True
                    break
                elif (x + d * j, y) not in clay and (x + d * j, y + 1) not in clay.union(still):
                    break
            borders[d] = x + d * j
        if dirs[-1] and dirs[1]:
            if (x, y) in flowing:
                flowing.remove((x, y))
            for xx in range(borders[-1] + 1, borders[1]):
                still.add((xx, y))
                if (xx, y) in flowing:
                    flowing.remove((xx, y))
            y -= 1
            continue

        elif dirs[-1]:
            for xx in range(borders[-1] + 1, borders[1] + 1):
                flowing.add((xx, y))
            if (borders[1], y) not in springs_seen:
                springs.add((borders[1], y))
        elif dirs[1]:
            for xx in range(borders[-1], borders[1]):
                flowing.add((xx, y))
            if (borders[-1], y) not in springs_seen:
                springs.add((borders[-1], y))
        else:
            for xx in range(borders[-1], borders[1] + 1):
                flowing.add((xx, y))
            if (borders[-1], y) not in springs_seen:
                springs.add((borders[-1], y))
            if (borders[1], y) not in springs_seen:
                springs.add((borders[1], y))
        break


# part I
flowing = {(x, y) for x, y in flowing if min_y <= y <= max_y}
print(len(flowing) + len(still))

# part II
print(len(still))