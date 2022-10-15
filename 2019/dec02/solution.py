with open("input") as f:
    program = list(map(int, f.read().split(',')))

def run(noun, verb, program):
    ip = 0
    program[1] = noun
    program[2] = verb
    while True:
        opcode = program[ip]
        a, b, c = program[ip + 1: ip + 4]
        if opcode == 1:
            program[c] = program[a] + program[b]
            ip += 4
        elif opcode == 2:
            program[c] = program[a] * program[b]
            ip += 4
        elif opcode == 99:
            return program[0]

# part I
print(run(12, 2, program[:]))

# part II
for noun in range(100):
    for verb in range(100):
        if run(noun, verb, program[:]) == 19690720:
            print(100 * noun + verb)
            

