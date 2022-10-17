from collections import defaultdict
from itertools import permutations


program = defaultdict(int)
with open("input") as f:
    for i, inst in enumerate(f.read().split(',')):
        program[i] = int(inst)


def run(p):
    i = 0
    base = 0
    while True:
        inst = str(p[i]).zfill(5)
        opcode = int(inst[3:])

        if inst[2] == '1':
            a = i + 1
        else:
            a = p[i + 1] if inst[2] == '0' else p[i + 1] + base
        if inst[1] == '1':
            b = i + 2
        else:
            b = p[i + 2] if inst[1] == '0' else p[i + 2] + base
        if inst[0] == '1':
            c = i + 3
        else:
            c = p[i + 3] if inst[0] == '0' else p[i + 3] + base

        if opcode == 1:
            p[c] = p[a] + p[b]
            i += 4
        elif opcode == 2:
            p[c] = p[a] * p[b]
            i += 4
        elif opcode == 3:
            p[a] = yield
            i += 2
        elif opcode == 4:
            yield p[a]
            i += 2
        elif opcode == 5:
            i = p[b] if p[a] else i + 3
        elif opcode == 6:
            i = p[b] if not p[a] else i + 3
        elif opcode == 7:
            p[c] = int(p[a] < p[b])
            i += 4
        elif opcode == 8:
            p[c] = int(p[a] == p[b])
            i += 4
        elif opcode == 9:
            base += p[a]
            i += 2
        if opcode == 99:
            return
          

# part I:
p = run(program)
next(p)
print(p.send(1))

# part II:
p = run(program)
next(p)
print(p.send(2))
