import re

from collections import defaultdict


with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


def intersection(a, b):
    out = []
    for i in [0, 2, 4]:
        out.extend([(m := max(a[i], b[i])), (M :=min(a[i + 1], b[i + 1]))])
        if m > M:
            return False
    return tuple(out)


def get_area(a, restrict):
    if restrict:
        a = intersection(a, (-50, 50, -50, 50, -50, 50))
    return (a[1] - a[0] + 1) * (a[3] - a[2] + 1) * (a[5] - a[4] + 1) if a else 0


def get_lights(lines, restrict):
    boxes = defaultdict(int)
    for mode, points in lines:
        p = tuple(map(int, re.findall("-?\d+", points)))
        for box, sign in dict(boxes).items():
            intersect = intersection(p, box)
            if intersect:
                boxes[intersect] -= sign
        if mode == 'on':
            boxes[p] += 1
    return sum(get_area(box, restrict) * sign for box, sign in boxes.items())


# part I
print(get_lights(lines, True))

# part II
print(get_lights(lines, False))
