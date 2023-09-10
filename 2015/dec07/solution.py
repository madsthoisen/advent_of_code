with open("input") as f:
    ins = [line.strip().split(' -> ') for line in f.readlines()]
    ins = {x[1]: x[0] for x in ins}


ops = {'AND': lambda a, b: a & b,
       'OR': lambda a, b: a | b,
       'LSHIFT': lambda a, b: a << b,
       'RSHIFT': lambda a, b: a >> b}


def f(w):
    if w in wires:
        return wires[w]
    elif w.isdigit():
        return int(w)
    i = ins[w].split(' ')
    if len(i) == 1:
        return f(i[0])
    elif len(i) == 2:
        return ~f(i[1])
    a, op, b = i
    wires[w] = ops[op](f(a), f(b))
    return wires[w]


# part I
wires = {}
out = f('a')
print(out)

# part II
wires = {'b': out}
print(f('a'))
