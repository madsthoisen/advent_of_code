import re

from itertools import count


with open("input") as f:
    points = [list(map(int, re.findall("\-*\d+", line))) for line in f.readlines()]


def show(points, min_x, max_x, min_y, max_y):
    rows = [
        "".join("#" if (x, y) in points else "." for x in range(min_x, max_x + 1))
        for y in range(min_y, max_y + 1)
    ]
    print("\n".join(rows))


for i in count(1):
    points = [[x + v_x, y + v_y, v_x, v_y] for x, y, v_x, v_y in points]
    min_x = min(x for x, y, _, _ in points)
    max_x = max(x for x, y, _, _ in points)
    min_y = min(y for x, y, _, _ in points)
    max_y = max(y for x, y, _, _ in points)
    if max_x - min_x < 75 and max_y - min_y < 75:
        show([(x, y) for x, y, _, _ in points], min_x, max_x, min_y, max_y)
        input(i)
