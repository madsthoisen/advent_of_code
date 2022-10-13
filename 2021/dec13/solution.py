with open("input") as f:
    a, b = f.read().strip().split("\n\n")


points = set(tuple(map(int, p.split(','))) for p in a.split('\n'))
for i, ins in enumerate(b.split("\n")):
    new_points = set()
    typ, val = ins.split()[-1].split('=')
    val = int(val)
    for x, y in points:
        if typ == 'x' and x > val:
            new_points.add((val - (x - val), y))
        elif typ == 'y' and y > val:
            new_points.add((x, val - (y - val)))
        else:
            new_points.add((x, y))
    points = new_points
    if not i:
        print(len(points))  # part I

# part II
x_max, y_max = max(x for x, _ in points), max(y for _, y in points)
for y in range(y_max + 1):
    print(''.join('#' if (x, y) in points else ' ' for x in range(x_max + 1)))
