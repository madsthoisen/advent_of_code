import re


with open("input") as f:
    strings, move = f.read().split("\n\n")
    lines = strings.split('\n')


def pwd(x, y, facing):
    vals = {-1: 2, 1: 0, 1j: 3, -1j: 1}
    return 1000 * (y + 1) + 4 * (x + 1) + vals[facing]


def x_border(y):
    if y < 50:
        return 50, 149
    if y < 100:
        return 50, 99
    if y < 150:
        return 0, 99
    return 0, 49


def y_border(x):
    if x < 50:
        return 100, 199
    if x < 100:
        return 0, 149
    return 0, 49


def get_surface(x, y):
    if y < 50:
        if x < 100:
            return 1
        return 2
    if y < 100:
        return 3
    if y < 150:
        if x < 50:
            return 4
        return 5
    if y < 200:
        return 6


def solve(pos, transitions):
    facing = 1
    trans = {'R': -1j, 'L': 1j, '': 1}
    moves = {1: (1, 0), -1: (-1, 0), 1j: (0, -1), -1j: (0, 1)}
    for move, d in zip(mm, dd):
        for _ in range(move):
            x, y = pos
            y0, y1 = y_border(x)
            x0, x1 = x_border(y)

            surface = get_surface(x, y)
            old_pos = pos
            old_facing = facing
            pos = (pos[0] + moves[facing][0], pos[1] + moves[facing][1])
            x, y = pos
            if y > y1 or y < y0 or x > x1 or x < x0:
                x, y, facing = transitions(x, y, facing, surface)
                pos = (x, y)
                if lines[y][x] == '#':
                    pos = old_pos
                    facing = old_facing
                    break
            if lines[y][x] == '#':
                pos = old_pos
                break

        facing *= trans[d]
    return pos, facing


_pos = next((i, y) for y, line in enumerate(lines) for i in range(len(line)) if line[i] == '.')
mm = list(map(int, re.findall("\d+", move)))
dd = list(re.findall("[LR]", move)) + ['']


# part I
def transitions(x, y, facing, surface):
    if facing == 1:   # moved right and out
        x, _ = x_border(y)
    elif facing == -1:   # moved left and out
        _, x = x_border(y)
    elif facing == -1j:   # moved down and out
        y, _ = y_border(x)
    elif facing == 1j:   # moved up and out
        _, y = y_border(x)
    return x, y, facing


pos, facing = solve(_pos, transitions)
print(pwd(pos[0], pos[1], facing))


# part II
def transitions(x, y, facing, surface):
    """
    The cube looks something like:
      1 2
      3
    4 5
    6
    """
    if surface == 1:
        if facing == 1j:  # up out of 1 -> into 6 from left
            y = x + 100
            x, _ = x_border(y)
            facing = 1
        elif facing == -1:  # left out of 1 -> into 4 from left
            y = 149 - y
            x, _ = x_border(y)
            facing = 1

    elif surface == 2:
        if facing == 1j:  # up out of 2 -> up into 6
            x = x - 100
            _, y = y_border(x)
            facing = 1j
        elif facing == -1j:  # down out of 2 -> into 3 from right
            y = x - 50
            _, x = x_border(y)
            facing = -1
        if facing == 1:  # right out of 2 -> into 5 from right
            y = 149 - y
            _, x = x_border(y)
            facing = -1

    elif surface == 3:
        if facing == -1:  # left out of 3 -> down into 4
            x = y - 50
            y, _ = y_border(x)
            facing = -1j
        elif facing == 1:  # right out of 3 -> up into 2
            x = 50 + y
            _, y = y_border(x)
            facing = 1j

    elif surface == 4:
        if facing == -1:  # left out of 4 -> into 1 from left
            y = 149 - y
            x, _ = x_border(y)
            facing = 1
        elif facing == 1j:  # up out of 4 -> into 3 from left
            y = x + 50
            x, _ = x_border(y)
            facing = 1

    elif surface == 5:
        if facing == 1:  #right out of 5 -> into 2 from right
            y = 149 - y
            _, x = x_border(y)
            facing = -1
        elif facing == -1j:  # down out of 5 -> into 6 from right
            y = x + 100
            _, x = x_border(y)
            facing = -1

    elif surface == 6:
        if facing == 1:  # right out of 6 -> up into 5
            x = y - 100
            _, y = y_border(x)
            facing = 1j
        elif facing == -1:  # left out of 6 -> down into 1
            x = y - 100
            y, _ = y_border(x)
            facing = -1j
        elif facing == -1j:  # down out of 6 -> down into 2
            x = x + 100
            y, _ = y_border(x)
            facing = -1j

    return x, y, facing


pos, facing = solve(_pos, transitions)
print(pwd(pos[0], pos[1], facing))
