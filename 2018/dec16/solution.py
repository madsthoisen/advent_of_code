import re

from collections import defaultdict


with open("input") as f:
    manual, program = f.read().split("\n\n\n")


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

possible_opcodes = {i: set(opcodes) for i in range(16)}
manual = [[list(map(int, re.findall("\d+", l))) for l in el.split("\n")] for el in manual.split("\n\n")]
behave_like_more_than_three = 0
for regs_before, (opcode, a, b, c), regs_after in manual:
    behave_like = 0
    for typ, op in opcodes.items():
        regs = list(regs_before)
        op(regs, a, b, c)
        if regs != regs_after:
             possible_opcodes[opcode] -= {typ}
        else:
            behave_like += 1
    if behave_like > 2:
        behave_like_more_than_three += 1

# part I
print(behave_like_more_than_three)
    
## part II
program = [list(map(int, l.split())) for l in program.strip().split("\n")]
while True:
    fixed = [(k, v) for k, v in possible_opcodes.items() if len(v) == 1]
    for k, v in possible_opcodes.items():
        for i, opcode in fixed:
            if i != k:
                possible_opcodes[k] = possible_opcodes[k] - opcode
    if all(len(v) == 1 for v in possible_opcodes.values()):
        opcodes = {k: opcodes[v.pop()] for k, v in possible_opcodes.items()}
        break

regs = [0, 0, 0, 0]
[opcodes[opcode](regs, a, b, c) for opcode, a, b, c in program]
print(regs[0])
