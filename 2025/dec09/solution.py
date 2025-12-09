from shapely.geometry import Polygon

with open("input") as f:
    reds = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


# part I
print(max(area(p, q) for p in reds for q in reds))

# part II
poly = Polygon(reds)
m = 0
for i, (x1, y1) in enumerate(reds):
    for (x2, y2) in reds[i + 1:]:
        mx, Mx = min(x1, x2), max(x1, x2)
        my, My = min(y1, y2), max(y1, y2)
        rect = Polygon([(mx, my), (Mx, my), (Mx, My), (mx, My)])
        if poly.intersection(rect).equals(rect):
            m = max(m, area((x1, y1), (x2, y2)))
print(m)
