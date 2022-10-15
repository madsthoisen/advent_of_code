import re

from sympy import divisors


def addr(r, a, b, c):
    r[c] = r[a] + r[b]

def addi(r, a, b, c):
    r[c] = r[a] + b

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]

def muli(r, a, b, c):
    r[c] = r[a] * b

def banr(r, a, b, c):
    r[c] = r[a] & r[b]

def bani(r, a, b, c):
    r[c] = r[a] & b

def borr(r, a, b, c):
    r[c] = r[a] | r[b]

def bori(r, a, b, c):
    r[c] = r[a] | b

def setr(r, a, b, c):
    r[c] = r[a]

def seti(r, a, b, c):
    r[c] = a

def gtir(r, a, b, c):
    r[c] = 1 if a > r[b] else 0

def gtri(r, a, b, c):
    r[c] = 1 if r[a] > b else 0

def gtrr(r, a, b, c):
    r[c] = 1 if r[a] > r[b] else 0

def eqir(r, a, b, c):
    r[c] = 1 if a == r[b] else 0

def eqri(r, a, b, c):
    r[c] = 1 if r[a] == b else 0

def eqrr(r, a, b, c):
    r[c] = 1 if r[a] == r[b] else 0


opcodes = {'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli, 
           'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori, 
           'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri, 
           'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr}

with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]
    bound = int(re.findall("\d+", tmp[0])[0])
    program = [x.split(' ') for x in tmp[1:]]
    program = [[p[0]] + list(map(int, p[1:])) for p in program]

def execute(regs, opcode, a, b, c):
    opcodes[opcode](regs, a, b, c)

def run(program, bound, regs=[0, 0, 0, 0, 0, 0]):
    pointer = regs[bound]
    while True:
        regs[bound] = pointer
        execute(regs, *program[pointer])
        pointer = regs[bound] + 1
        if pointer >= len(program):
            return regs[0]

# part I
print(f"part 1: {run(program, bound)}")

# part II
# Analyzing the program by hand, reveals that the answer is the sum of the divisors of 10551287
print(f"part 2: {sum(divisors(10551287))}")
