with open("input") as f:
    lines = [line.strip().split(' -> ') for line in f.readlines()]


rock = set()
max_y = 0
for ll in lines:
    for i in range(len(ll) - 1):
        x0, y0 = map(int, ll[i].split(','))
        x1, y1 = map(int, ll[i + 1].split(','))
        if x1 == x0:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                rock.add((x0, y))
        elif y1 == y0:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                rock.add((x, y0))
        max_y = max(y, max_y)
        x0, y0 = x1, y1


def sim(part):
    rest = set()
    while True:
        u = rest.union(rock)
        x, y = 500, 0
        flowing = True
        while flowing:
            if y > max_y and part == 1:
                return len(rest)
            flowing = False
            for i in [0, -1, 1]:
                if (x + i, y + 1) not in u:
                    if not part == 2 or part == 2 and y + 1 <= max_y + 1:
                        x += i
                        y += 1
                        flowing = True
                        break
        rest.add((x, y))
        if (500, 0) in rest and part == 2:
            return len(rest)


# part I
print(sim(part=1))

# part II
print(sim(part=2))
