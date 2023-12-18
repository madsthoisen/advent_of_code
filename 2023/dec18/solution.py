with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


def get_area(part2):
    area = 0
    xn, yn = 0, 0
    n_points = 0
    for direction, d, code in lines:
        d = int(d)
        if part2:
            d = int(code[2:-2], 16)
            direction = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(code[-2], 16)]
        xo, yo = xn, yn
        n_points += int(d)
        if direction == 'L':
            xn = xo - d
        elif direction == 'R':
            xn = xo + d
        elif direction == 'U':
            yn = yo + d
        elif direction == 'D':
            yn = yo - d
        area += xn * yo - xo * yn
    return abs(area) // 2 + n_points // 2 + 1


# part I
print(get_area(False))

# part II
print(get_area(True))
