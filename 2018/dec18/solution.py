from itertools import product, count


with open("input") as f:
    area = [list(line.strip()) for line in f.readlines()]


def get_adj(area, r, c):
    h, w = len(area), len(area[0])
    adj = {'.': 0, '|': 0, '#': 0}
    increments = ((i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0))
    for i, j in increments:
        r_, c_ = r + i, c + j
        if 0 <= r_ < h and 0 <= c_ < w:
            adj[area[r_][c_]] += 1
    return adj


def next_round(area):
    new_area = []
    for r in range(len(area)):
        row = []
        for c in range(len(area[0])):
            adj = get_adj(area, r, c)
            p = area[r][c]
            if p == '.' and adj['|'] >= 3:
                    row.append('|')
                    continue
            if p == '|' and adj['#'] >= 3:
                    row.append('#')
                    continue
            if p == '#' and not (adj['#'] > 0 and adj['|'] > 0):
                    row.append('.')
                    continue
            row.append(p)
        new_area.append(row)
    return new_area


def count_after_min(area, minutes):
    area_ = area
    for _ in range(minutes):
        area_ = next_round(area_)
    trees = sum((x == '|') for r in range(len(area_)) for x in area_[r])
    lumber_yards = sum((x == '#') for r in range(len(area_)) for x in area_[r])
    return trees * lumber_yards


# part I
print(count_after_min(area, 10))

# part II
seen = {}
minutes = 1_000_000_000
area_ = area
for minute in count(1):
    area_ = next_round(area_)
    tuple_area = tuple([tuple(x) for x in area_])
    if tuple_area in seen:
        rem = (minutes - minute) % (minute - seen[tuple_area])
        print(count_after_min(area_, rem))
        break
    seen[tuple_area] = minute
