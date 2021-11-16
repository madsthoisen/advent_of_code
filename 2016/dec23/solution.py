with open("input") as f:
    instructions = [line.strip().split(' ') for line in f.readlines()]

# part I
eggs = 7
registers = {chr(97 + i): 0 for i in range(4)}
registers['a'] = eggs
i = 0
toggled = set()
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
        if ins == 'jnz':
            try:
                y = int(y)
            except:
                y = int(registers[y])
            if x != 0:
                i += int(y)
                continue
    i += 1
print(registers['a'])

# part II
print(12*11*10*9*8*7*6*5*4*3*2 + 81*93)
