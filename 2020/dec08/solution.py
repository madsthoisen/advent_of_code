import copy

with open ("input") as f:
    ins = [line.strip().split(" ") for line in f.readlines()]

def proc(ins, p, acc):
    x = ins[p]
    if x[0] == "nop":
        p += 1
    elif x[0] == "jmp":
        p += int(x[1])
    elif x[0] == "acc":
        p += 1
        acc += int(x[1])
    return p, acc

def run(ins, p, acc):
    visited = set()
    acc, p = 0, 0
    while True:
        visited.add(p)
        old = acc
        p, acc = proc(ins,p, acc)
        if p == len(ins):
            return True, acc
        p %= len(ins)
        if p in visited:
            return False, old

# part I
print(run(ins, 0, 0))

# part II
for i in range(len(ins)):
    ins_tmp = copy.deepcopy(ins)
    if ins[i][0] == "jmp":
       ins_tmp[i][0] = "nop"
    elif ins[i][0] == "nop":
       ins_tmp[i][0] = "jmp"
    terminates, acc = run(ins_tmp, 0, 0)
    if terminates:
        print(acc)
        break
