import numpy as np

from functools import cmp_to_key


with open("input") as f:
    blocks = [list(map(eval, block.split("\n"))) for block in f.read().split('\n\n')]


def cmp(a, b):
    if not a:
        if not b:
            return 0
        return -1
    for i in range(len(a)):
        if i >= len(b):
            return 1
        x, y = a[i], b[i]
        if isinstance(x, int) and isinstance(y, int):
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                c = 0
        else:
            c = cmp([x] if isinstance(x, int) else x, [y] if isinstance(y, int) else y)
        if c != 0:
            return c
    if i < len(b) - 1:
        return -1
    return 0


# part I
print(sum(i + 1 for i, (a, b) in enumerate(blocks) if cmp(a, b) != 1))

# part II
all_blocks = sorted([[[2]], [[6]]] + [x for b in blocks for x in b], key=cmp_to_key(cmp))
print(np.prod([(i + 1) for i, b in enumerate(all_blocks) if b in [[[2]], [[6]]]]))

