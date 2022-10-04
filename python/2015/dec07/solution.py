with open("input") as f:
    tmp = [line.strip().split(" -> ") for line in f.readlines()]

ins = {l[1]: l[0] for l in tmp}
out = {}
def f(wire):
    if wire in out:
        return out[wire]
    cmd = ins[wire].split(' ')
    if len(cmd) == 1:
        w = cmd[0]
        out[wire] = int(w) if w.isdigit() else f(w)
        return out[wire]
    if cmd[0] == "NOT":
        out[wire] = f(cmd[1])^65535
        return out[wire]
    a, op, b = cmd
    a = int(a) if a.isdigit() else f(a)
    b = int(b) if b.isdigit() else f(b)
    if op == "AND":
        o =  a & b 
    elif op == "OR":
        o =  a | b
    elif op == "LSHIFT":
        o =  a << b
    elif op == "RSHIFT":
        o =  a >> b
    out[wire] = o
    return out[wire]

# part I
print(part1 := f('a'))

# part II
out = {'b': part1}
print(f('a'))
