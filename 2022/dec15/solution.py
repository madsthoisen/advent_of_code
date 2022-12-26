import re


with open("input") as f:
    lines = [map(int, re.findall("-?\d+", line)) for line in f.readlines()]


def combine_intervals(a):
    b = []
    for begin, end in sorted(a):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b


circles = [((sx, sy), abs(bx - sx) + abs(by - sy)) for sx, sy, bx, by in lines]

for y in range(0, 4_000_000 + 1):
    blocked = [(cx - r + abs(y - cy), cx + r - abs(y - cy)) for (cx, cy), r in circles if cy - r <= y <= cy + r]
    blocked = combine_intervals(blocked)
    # part I
    if y == 2_000_000:
        print(sum(x[1] - x[0] for x in combine_intervals(blocked)))
    # part II
    if len(blocked) > 1:
        print(4_000_000 * (blocked[0][1] + 1) + y)



