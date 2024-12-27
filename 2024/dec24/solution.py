import itertools
import random

from operator import and_, or_, xor


with open("input") as f:
    reg, _prog = [block.split("\n") for block in f.read().split("\n\n")]


prog = {}
N = -1
for ll in _prog:
    a, c = ll.split(' -> ')
    prog[c] = a.split(' ')
    if c[0] == "z":
        N = max(N, int(c[1:]) + 1)


def get_z(regs):
    return int(''.join(str(regs['z' + str(i).zfill(2)]) for i in range(N))[::-1], 2)


def run(regs, pp):
    pp = pp.copy()
    while pp:
        old_len = len(pp)
        for c, (a, op, b) in pp.items():
            if a in regs and b in regs:
                regs[c] = int({"AND": and_, "OR": or_, "XOR": xor}[op](regs[a], regs[b]))
                del pp[c]
                break
        if len(pp) == old_len:
            return False
    return regs


def test(prog):
    for _ in range(5):
        a, b = (random.randint(2**(N - 2), 2**(N - 1)) for _ in range(2))
        x_bin = bin(a)[2:].zfill(N)
        y_bin = bin(b)[2:].zfill(N)
        regs = {}
        for i, (x, y) in enumerate(zip(x_bin[::-1], y_bin[::-1])):
            regs['x' + str(i).zfill(2)] = int(x)
            regs['y' + str(i).zfill(2)] = int(y)
        regs = run(regs, prog)
        if not regs:
            return False
        if get_z(regs) != a + b:
            return False
    return True


# part I
regs_p1 = {}
for ll in reg:
    a, b = ll.split(": ")
    regs_p1[a] = int(b)
print(get_z(run(regs_p1, prog)))

# part II
wrong = [c for c, (_, op, _) in prog.items() if c[0] == "z" and op != "XOR"]
swaps = []
for w in wrong:
    x = w.replace('z', 'x')
    y = w.replace('z', 'y')
    for c, (a, op, b) in prog.items():
        if (a, b) == (x, y) or (b, a) == (x, y):
            search = c
            for res, (a, op, b) in prog.items():
                if op == "XOR" and (a == c or b == c):
                    swaps.append((w, res))
for a, b in swaps:
    prog[b], prog[a], = prog[a], prog[b]
for a, b in itertools.combinations(prog.keys(), 2):
    _prog = prog.copy()
    _prog[a], _prog[b] = prog[b], prog[a]
    if test(_prog):
        swaps.append((a, b))
        break
print(','.join(sorted([s for swap in swaps for s in swap])))
