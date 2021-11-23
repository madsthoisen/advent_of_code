from collections import defaultdict
from copy import deepcopy


with open("input") as f:
    points = {tuple(map(int, line.strip().split(','))) for line in f.readlines()}


def perimeter(size):
    for i in {-size, size}:
        for j in range(-size, size + 1):
            yield (i, j)
            if j not in {-size, size}:
                yield (j, i)


m = max(max(x) for x in points)
old_areas = defaultdict(int)
largest_area = 0
part_2 = 0
for size in range(2*m):
    areas = deepcopy(old_areas)
    for (x, y) in perimeter(size):
        dist = {p : abs(p[0] - x) + abs(p[1] - y) for p in points}
        if sum(dist.values()) < 10000:
            part_2 += 1
        if len(minima := [key for key, val in dist.items() if val == min(dist.values())]) == 1:
            areas[minima[0]] += 1

    for key, val in areas.items():
        if old_areas.get(key) == val:
            largest_area = max(largest_area, val)
    old_areas = deepcopy(areas)

# part I
print(largest_area)

# part II
print(part_2)
