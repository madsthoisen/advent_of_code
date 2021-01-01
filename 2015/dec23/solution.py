with open("input") as f:
    ins = {i: l.strip().replace(',', '').split(' ') for i, l in
            enumerate(f.readlines())}

def round(p, regs):
    i, rest = ins[p][0], ins[p][1:]
    if i == 'hlf':
        regs[rest[0]] /= 2
        return p + 1, regs
    if i == 'tpl':
        regs[rest[0]] *= 3
        return p + 1, regs
    if i == 'inc':
        regs[rest[0]] += 1
        return p + 1, regs
    if i == 'jmp':
        return p + int(rest[0]), regs
    if i == 'jie':
        if not regs[rest[0]] % 2:
            return p + int(rest[1]), regs
        else:
            return p + 1, regs
    if i == 'jio':
        if regs[rest[0]] == 1:
            return p + int(rest[1]), regs
        else:
            return p + 1, regs

def program(regs, ins):
    p = 0
    while True:
        p, regs = round(p, regs)
        if p not in ins:
            return regs['b']

# part I
regs = {'a': 0, 'b': 0}
print(program(regs, ins))

# part II
regs = {'a': 1, 'b': 0}
print(program(regs, ins))
