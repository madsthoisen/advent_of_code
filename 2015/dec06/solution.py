from copy import deepcopy

with open("input") as f:
    tmp = [line.strip().split(' through ') for line in f.readlines()]
    cmds = [(l[0].split(' ') + [l[1]])[-3:] for l in tmp]

def f(l, c):
    if c == "on":
        return 1
    if c == "off":
        return 0
    return (l + 1) % 2

def g(l, c):
    if c == "on":
        return l + 1
    if c == "off":
        return max(0, l - 1)
    return l + 2

def lights(grid, cmds, fct):
    for cmd in cmds:
        i0, i1 = list(map(int, cmd[1].split(',')))
        j0, j1 = list(map(int, cmd[2].split(',')))
        for i in range(i0, j0 + 1):
            for j in range(i1, j1 + 1):
                grid[i][j] = fct(grid[i][j], cmd[0])
    return grid

grid = [[0 for _ in range(1000)] for _ in range(1000)]

# part I
grid_1 = lights(deepcopy(grid), cmds, f)
print(sum(sum(line) for line in grid_1))

# part II
grid_2 = lights(deepcopy(grid), cmds, g)
print(sum(sum(line) for line in grid_2))

