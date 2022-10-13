with open("input") as f:
    dirs = [(i[0], int(i[1:])) for i in map(lambda s: s.strip(), f.readlines())]

directions = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
rotations = {'L': 1j, 'R': -1j}

def part1():
    loc = 0
    d = 1
    for r, a in dirs:
        if r in directions.keys():
            loc += a * directions[r]
        elif r in rotations.keys():
            d *= rotations[r]**(a // 90)
        elif r == 'F':
            loc += a * d
    return int(abs(loc.real) + abs(loc.imag))

def part2():
    wp = 10 + 1j
    ship = 0
    for r, a in dirs:
        if r in directions.keys():
            wp += a * directions[r]
        elif r in rotations.keys():
            wp *= rotations[r]**(a // 90)
        elif r == 'F':
            ship += a * wp
    return int(abs(ship.real) + abs(ship.imag))

# part I
print(part1())

# part II
print(part2())

