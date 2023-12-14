from copy import deepcopy


with open("input") as f:
    grids = [[list(x) for x in b.split("\n")] for b in f.read().split("\n\n")]


def get_mirror(g, ignore=None):
    rows = len(g)
    for r in range(rows):
        refl = [g[r - i] == g[r + i - 1] for i in range(1, min(r, rows - r) + 1)]
        if refl and all(refl) and r != ignore:
            return r
    return 0


def smudge(g, h, v):
    for c in range(len(g[0])):
        for r in range(len(g)):
            g_tmp = deepcopy(g)
            g_tmp[r][c] = "." if g_tmp[r][c] == "#" else "."
            new_h = get_mirror(g_tmp, h)
            new_v = get_mirror(list(zip(*g_tmp)), v)
            if new_h != 0 or new_v != 0:
                return new_h, new_v


part1, part2 = 0, 0
for grid in grids:
    h_res, v_res = get_mirror(grid), get_mirror((list(zip(*grid))))
    part1 += 100 * h_res + v_res

    new_h_res, new_v_res = smudge(grid, h_res, v_res)
    part2 += 100 * new_h_res + new_v_res

# part I
print(part1)

# part II
print(part2)
