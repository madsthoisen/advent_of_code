with open("input") as f:
    w1, w2 = f.read().strip().split('\n')


def build(w):
    p = 0
    wire = {}
    i = 0
    for instr in w.split(','):
        d, dist = instr[0], int(instr[1:])
        dirs = {'L': -1, 'R': 1, 'U': 1j, 'D': -1j}
        for _ in range(dist):
            i += 1
            p += dirs[d]
            if p not in wire:
                wire[p] = i
    return wire

w1, w2 = build(w1), build(w2)
intersections = set(w1.keys()) & set(w2.keys())

# part I        
print(min(abs(x.real) + abs(x.imag) for x in intersections))

# part II
print(min(w1[x] + w2[x] for x in intersections))





