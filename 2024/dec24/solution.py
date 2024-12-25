import re
import matplotlib.pyplot as plt
import itertools
import random

import networkx as nx


with open("input") as f:
    a, b = [bl.split("\n") for bl in f.read().split("\n\n")]


bits = {}
for line in a:
    x, y = line.split(': ')
    bits[x] = True if y == "1" else False

instructions = {}
for line in b:
    x, res = line.split(' -> ')
    instructions[res] = tuple(x.split(' '))

def get_binary(s, bits, lim=None):
    res = []
    for k in sorted(bits):
        v = bits[k]
        if k.startswith(s):
            res.append((int(k[1:]), v))
    if lim:
        res = res[:lim]
    return ''.join(str(int(x)) for _, x in sorted(res, reverse=True))


# part I
def run(instructions, bits):
    i = 0
    keys = sorted(instructions.keys())
    while keys:
        res = keys[i]
        a, op, b = instructions[res]
        if a in bits and b in bits:
            a, op, b = instructions[res]
            if op == 'AND':
                bits[res] = bits[a] and bits[b]
            if op == "OR":
                bits[res] = bits[a] or bits[b]
            if op == "XOR":
                bits[res] = bits[a] != bits[b]
            keys.pop(i)
            i = 0
        else:
            i += 1
    return bits


# part II
bits = run(instructions, bits)
ans = get_binary("z", bits)
print(int(ans, 2))

# part II
def build(ins, bits):
    i = 0
    keys = sorted(ins.keys())
    g = {k: k for k in bits}
    G_and = nx.DiGraph()
    G_or = nx.DiGraph()
    G_xor = nx.DiGraph()
    while keys:
        res = keys[i]
        a, op, b = ins[res]
        if a in g and b in g:
            a, op, b = ins[res]
            if op == "AND":
                g[res] = g[a] and g[b]
                G_and.add_edge(a, res)
                G_and.add_edge(b, res)
            if op == "OR":
                g[res] = g[a] or g[b]
                G_or.add_edge(a, res)
                G_or.add_edge(b, res)
            if op == "XOR":
                g[res] = g[a] != g[b]
                G_xor.add_edge(a, res)
                G_xor.add_edge(b, res)
            try:
                ia = str(int(g[a][1:]))
                ib = str(int(g[a][1:]))
                assert ia == ib
                g[res] = ia+ib+op
            except:
                g[res] = (g[a], op, g[b])

            keys.pop(i)
            i = 0
        else:
            i += 1
    print(G_xor.edges)
    print(nx.ancestors(G_xor, "z00"))
    for i in range(45):
        for j in range(45):
            a = get_bit('x', i)
            b = get_bit('z', j)
            if a in G_xor and b in G_xor and nx.has_path(G_xor, a, b):
                path = nx.shortest_path(G_xor, a, b)
                print("xor path", a, b, path)
            if a in G_or and b in G_or and nx.has_path(G_or, a, b):
                path = nx.shortest_path(G_or, a, b)
                print("or path", a, b, path)
            if a in G_and and b in G_and and nx.has_path(G_and, a, b):
                path = nx.shortest_path(G_and, a, b)
                print("and path", a, b, path)
    return g

def run_ab(instructions, x, y):
    try:
        i = 0
        keys = sorted(instructions.keys())
        bits = {}
        for i, val in enumerate(x):
            bits['x' + str(i).zfill(2)] = int(val)
        for i, val in enumerate(y):
            bits['y' + str(i).zfill(2)] = int(val)
        while keys:
            res = keys[i]
            a, op, b = instructions[res]
            if a in bits and b in bits:
                a, op, b = instructions[res]
                if op == 'AND':
                    bits[res] = bits[a] and bits[b]
                if op == "OR":
                    bits[res] = bits[a] or bits[b]
                if op == "XOR":
                    bits[res] = bits[a] != bits[b]
                keys.pop(i)
                i = 0
            else:
                i += 1
        return bits
    except IndexError:
        return None


def get_bit(s, n):
    return s + str(n).zfill(2)

bits = {get_bit(s, i) for s in ['x', 'y'] for i in range(45)}
g = build(instructions, bits)
#z00 = ('x00', 'XOR', 'y00')
#for k, v in g.items():

#i = 0
#for k, v in g.items():
#    if k.startswith("z"):
#        i += 1
#        nums = list(map(int, re.findall(r"\d+", v.__repr__())))
#        print(sorted(set(nums)))
#        print(k, v)

# frn, z05
#import random

# swapping the following did not work
# frn, z05
# z21, gmq
# z39, wtt
candidates = [k for k in instructions.keys() if not k.startswith('x') and not k.startswith('y')]
pairs = [(candidates[i], candidates[j]) for i in range(len(candidates)) for j in range(i + 1, len(candidates))]
for comb in itertools.combinations(pairs, 4):

    new_instructions = dict(instructions)
    for a in comb:
        new_instructions[a[0]] = instructions[a[1]]
        new_instructions[a[1]] = instructions[a[0]]
    aa = random.randint(0, 2**43)
    bb = random.randint(0, 2**43)
    x = bin(aa)[2:].zfill(45)
    y = bin(bb)[2:].zfill(45)
    bits = run_ab(new_instructions, x, y)
    if bits is not None:
        ans_bin = get_binary('z', bits)
        ans_bin_reversed = ans_bin[::-1]
        ans = int(ans_bin, 2)
        ans_reversed = int(ans_bin_reversed, 2)
        if ans == aa + bb or ans_reversed == aa + bb:
            print("found", comb)
            break
