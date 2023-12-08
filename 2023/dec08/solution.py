from itertools import count
from math import gcd


def lcm(ll):
    _lcm = 1
    for x in ll:
        _lcm = _lcm * x // gcd(_lcm, x)
    return _lcm


with open("input") as f:
    ins, mm = f.read().split("\n\n")

lines = [x.strip().split(' = ') for x in mm.split("\n")]
d = {a: rest[1:-1].split(', ') for a, rest in lines}


def get(part2=False):
    ll = []
    start = [x for x in d if x[-1] == 'A'] if part2 else ['AAA']
    for curr in start:
        for i in count(0):
            curr = d[curr][0 if ins[i % len(ins)] == 'L' else 1]
            if curr == "ZZZ" and not part2:
                return i + 1
            if curr[-1] == "Z" and part2:
                ll.append(i + 1)
                break
    return lcm(ll)


# part I
print(get())

# part II
print(get(True))
