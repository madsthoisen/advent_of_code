with open("input") as f:
    instructions = [line.strip().split(' ') for line in f.readlines()]


# part I
registers = {chr(97 + i): 0 for i in range(4)}
i = 0
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
    else:
        try:
            x = int(x)
        except:
            x = int(registers[x])
        if ins == 'cpy':
            registers[y] = x
        if ins == 'jnz':
            if x != 0:
                i += int(y)
                continue
    i += 1
print(registers['a'])

# part II
def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)

print(fib(35) + 18*17)
