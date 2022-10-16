with open("input") as f:
    program = list(map(int, f.read().split(',')))


def run(p, ID):
    i = 0
    while True:
        inst = str(p[i]).zfill(5)
        opcode = int(inst[3:])
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
            p[a] = ID
            i += 2
        elif opcode == 4:
            out = p[a]
            i += 2
        elif opcode == 5:
            i = p[b] if p[a] else i + 3
        elif opcode == 6:
            i = p[b] if not p[a] else i + 3
        elif opcode == 7:
            print(inst)
            p[c] = int(p[a] < p[b])
            i += 4
        elif opcode == 8:
            p[c] = int(p[a] == p[b])
            i += 4
        if opcode == 99:
            print(out)
            return

# part I:
run(program[:], 1)

# part II:
run(program[:], 5)
