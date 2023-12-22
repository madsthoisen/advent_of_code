with open("input") as f:
    lines = [line.strip().split("~") for line in f.readlines()]


def get_occupied(bb):
    occupied = set()
    for (x1, y1, z1), (x2, y2, z2) in bb:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    occupied.add((x, y, z))
    return occupied


def get_new_bricks(bb):
    bb = sorted(bb, key=lambda x: x[0][2])
    occupied = get_occupied(bb)
    new_bb = []
    for (x1, y1, z1), (x2, y2, z2) in bb:
        inc = 0
        while z1 - inc > 1:
            inc += 1
            fill = {(x, y, z1 - inc) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}

            if len(fill & occupied) > 0:
                inc -= 1
                break
        new_b = ((x1, y1, z1 - inc), (x2, y2, z2 - inc))
        occupied -= get_occupied([((x1, y1, z1), (x2, y2, z2))])
        occupied |= get_occupied([new_b])

        new_bb.append(new_b)
    return new_bb


def stable(bb):
    occupied = get_occupied(bb)
    bb = sorted(bb, key=lambda x: x[0][2])
    for (x1, y1, z1), (x2, y2, z2) in bb:
        if z1 - 1 > 0:
            fills = {(x, y, z1 - 1) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}
            if len(fills & occupied) == 0:
                return False
    return True


bricks = [(list(map(int, a.split(','))), list(map(int, b.split(',')))) for a, b in lines]

# part I
bricks = get_new_bricks(bricks)
print(sum(stable(bricks[:i] + bricks[i + 1:]) for i in range(len(bricks))))

# part II
add = 0
for i in range(len(bricks)):
    tmp_bricks = bricks[:i] + bricks[i+1:]
    tmp_bricks_settled = get_new_bricks(tmp_bricks)
    add += sum(a != b for a, b in zip(sorted(tmp_bricks), sorted(tmp_bricks_settled)))
print(add)