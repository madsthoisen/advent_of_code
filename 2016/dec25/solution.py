with open("input") as f:
    instructions = [line.strip().split(' ') for line in f.readlines()]

# part I
# cheeky stoping criteria
a = 1
while True:
    registers = {chr(97 + i): 0 for i in range(4)}
    registers['a'] = a
    i = 0
    toggled = set()
    clock = []
    while -1 < i < len(instructions):
        instruction = instructions[i]
        if len(instruction) == 2:
            ins, x = instruction
        else:
            ins, x, y = instruction
        if ins == 'inc':
            registers[x] += 1
        elif ins == 'dec':
            registers[x] -= 1
        elif ins == 'tgl':
            x = registers[x]
            if i + x < len(instructions) and i + x not in toggled:
                toggled.add(i + x)
                instr = instructions[i + x]
                if len(instr) == 2:
                    instructions[i + x][0] = 'dec' if instr[0] == "inc" else "inc"
                else:
                    instructions[i + x][0] = "cpy" if instr[0] == "jnz" else "jnz"
        else:
            try:
                x = int(x)
            except:
                x = int(registers[x])
            if ins == 'cpy':
                registers[y] = x
            if ins == 'out':
                clock.append(x)
                if clock == [0, 1]*10:
                    print(a)
                    assert False
                if len(clock) > 1 and clock[-1] == clock[-2]:
                    break
            if ins == 'jnz':
                try:
                    y = int(y)
                except:
                    y = int(registers[y])
                if x != 0:
                    i += int(y)
                    continue
        i += 1
    a += 1
