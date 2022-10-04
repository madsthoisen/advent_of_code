import re

from collections import defaultdict


with open("input") as f:
    manual, program = f.read().split("\n\n\n")


def addr(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] + r[b]
    return r_

def addi(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] + b
    return r_

def mulr(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] * r[b]
    return r_

def muli(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] * b
    return r_

def banr(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] & r[b]
    return r_

def bani(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] & b
    return r_

def borr(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] | r[b]
    return r_

def bori(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a] | b
    return r_

def setr(r, a, b, c):
    r_ = list(r)
    r_[c] = r[a]
    return r_

def seti(r, a, b, c):
    r_ = list(r)
    r_[c] = a
    return r_

def gtir(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if a > r[b] else 0
    return r_

def gtri(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if r[a] > b else 0
    return r_

def gtrr(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if r[a] > r[b] else 0
    return r_

def eqir(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if a == r[b] else 0
    return r_

def eqri(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if r[a] == b else 0
    return r_

def eqrr(r, a, b, c):
    r_ = list(r)
    r_[c] = 1 if r[a] == r[b] else 0
    return r_


possibilities = {'addr': addr, 
                 'addi': addi,
                 'mulr': mulr,
                 'muli': muli, 
                 'banr': banr, 
                 'bani': bani, 
                 'borr': borr, 
                 'bori': bori, 
                 'setr': setr, 
                 'seti': seti, 
                 'gtir': gtir, 
                 'gtri': gtri, 
                 'gtrr': gtrr, 
                 'eqir': eqir, 
                 'eqri': eqri, 
                 'eqrr': eqrr}


opcodes = {i: set(possibilities.keys()) for i in range(16)}
manual = [list(map(int, re.findall("\d+", t))) for t in manual.split('\n\n')]
behave_like_more_than_three = 0
for item in manual:
    before = item[:4]
    opcode, a, b, reg = item[4 : 8]
    after = item[8:]
    behave_like = 0
    for typ, op in possibilities.items():
        tmp = op(before, a, b, reg)
        if after != tmp:
             opcodes[opcode] -= {typ}
        else:
            behave_like += 1
    if behave_like > 2:
        behave_like_more_than_three += 1

# part I
print(behave_like_more_than_three)

## part II
while True:
    for k, v in opcodes.items():
        if len(v) == 1:
            new_opcodes = {k: v for k, v in opcodes.items()}
            for k_, v_ in opcodes.items():
                if k_ != k:
                    new_opcodes[k_] -= v
    opcodes = {k: v for k, v in new_opcodes.items()}
    if all(len(v) == 1 for v in opcodes.values()):
        break

opcodes = {k: list(v)[0] for k, v in opcodes.items()}
regs = [0, 0, 0, 0]
for ins in program.strip().split("\n"):
    opcode, a, b, reg = list(map(int, ins.split()))
    op = possibilities[opcodes[opcode]]
    regs = op(regs, a, b, reg)
print(regs[0])
