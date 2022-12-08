with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


def get_vis(xy, x, y, a, b, d):
    if a == b:
        return 0, True
    for vd, i in enumerate(range(a, b, d)):
        g = grid[y][i] if xy == 'y' else grid[i][x]
        if g >= grid[y][x]:
            return vd + 1, False
    return vd + 1, True


w, h = len(lines[0]), len(lines)
grid = [list(map(int, l)) for l in lines]
visibles = 0
max_scenic_score = 0
for y in range(h):
    for x in range(w):
        vd_l, l = get_vis('y', x, y, x - 1, -1, -1)
        vd_r, r = get_vis('y', x, y, x + 1, w, 1)
        vd_u, u = get_vis('x', x, y, y - 1, -1, -1)
        vd_d, d = get_vis('x', x, y, y + 1, h, 1)

        max_scenic_score = max(max_scenic_score, vd_l * vd_r * vd_u * vd_d)
        visibles += any((l, r, u, d))

# part I
print(visibles)

# part II
print(max_scenic_score)
