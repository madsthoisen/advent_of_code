from math import inf


with open("input") as f:
    regs, prog = f.read().split("\n\n")


def get_combo(operand, regs):
    if operand <= 3:
        return operand
    return regs[{4: 'A', 5: 'B', 6: 'C'}[operand]]


def run(prog, regs):
    p = 0
    out = []
    while p + 1 < len(prog):
        opcode, operand = prog[p], prog[p + 1]
        lit = operand
        combo = get_combo(operand, regs)
        if opcode == 0:  # adv
            regs['A'] = regs['A'] // 2**combo
        if opcode == 1:  # bxl
            regs['B'] = regs['B'] ^ lit
        if opcode == 2:  # bst
            regs['B'] = combo % 8
        if opcode == 3:  # jnz
            if regs['A'] != 0:
                p = lit
                continue
        if opcode == 4:  # bxc
            regs['B'] = regs['B'] ^ regs['C']
        if opcode == 5:  # out
            value = combo % 8
            out.append(value)
        if opcode == 6:  # bdv
            regs['B'] = regs['A'] // 2**combo
        if opcode == 7:  # cdv
            regs['C'] = regs['A'] // 2**combo
        p += 2
    return out


def run_a(a, regs):
    regs['A'] = a
    return run(prog, regs.copy())


# part I
regs = {reg[9]: int(reg[11:]) for reg in regs.split("\n")}
prog = list(map(int, prog[9:].split(',')))
print(','.join(str(x) for x in run(prog, regs.copy())))

# part II
ans = inf
starts = list(range(10))
while starts:
    newstarts = set()
    for start in starts:
        for add in range(10):
            beg = str(start) + str(add)
            for lh in ['0', '9']:
                a = int(beg + lh * (14 - len(str(start))))
                res = run_a(a, regs)
                idx = 17 - len(beg)
                if len(res) == len(prog) and res[idx:] == prog[idx:]:
                    newstarts.add(beg)
                if res == prog:
                    ans = min(ans, a)

    starts = newstarts


print(ans)
