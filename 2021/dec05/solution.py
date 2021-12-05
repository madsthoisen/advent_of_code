from collections import defaultdict

with open("input") as f:
    lines = [line.strip().split(' -> ') for line in f.readlines()]


def get_overlap(include_diagonals):
    points = defaultdict(int)
    for x, y in lines:
        x1, y1 = list(map(int, x.split(',')))
        x2, y2 = list(map(int, y.split(',')))
        x_range = range(x1, x2 + 1) if  x1 < x2 else range(x1, x2 - 1, -1)
        y_range = range(y1, y2 + 1) if  y1 < y2 else range(y1, y2 - 1, -1)
        if x1 == x2:
            for y in y_range:
                points[(x1, y)] += 1
        elif y2 == y1:
            for x in x_range:
                points[(x, y2)] += 1
        if include_diagonals and x1 != x2 and y1 != y2:
            for x, y in zip(x_range, y_range):
                points[(x, y)] += 1
    return sum(1 for v in points.values() if v > 1)


# part I
print(get_overlap(False))

# part II
print(get_overlap(True))
