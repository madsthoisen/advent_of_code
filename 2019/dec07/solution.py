from itertools import permutations


with open("input") as f:
    program = list(map(int, f.read().split(',')))


def run(p):
    i = 0
    while True:
        inst = str(p[i]).zfill(5)
        opcode = int(inst[3:])
        if i + 1 < len(p):
            a = p[i + 1] if int(inst[2]) == 0 else i + 1
        if i + 2 < len(p):
            b = p[i + 2] if int(inst[1]) == 0 else i + 2
        if i + 3 < len(p):
            c = p[i + 3] if int(inst[0]) == 0 else i + 3
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
        if opcode == 99:
            return
          

# part I:
m = 0
for permutation in permutations(range(5)):
    signal = 0
    for x in permutation:
        p = run(program[:])
        next(p)
        p.send(x)
        signal = p.send(signal)
    m = max(m, signal)
print(m)

# part II

m = 0
for permutation in permutations(range(5, 10)):
    
    # Initialization
    programs = []
    for val in permutation:
        p = run(program[:])
        next(p)
        p.send(val)
        programs.append(p)

    signal = 0
    while True:
        try:
            for p in programs:
                signal = p.send(signal)
            [next(p) for p in programs]
        except StopIteration:
            m = max(m, signal)
            break
print(m)

