import re
import numpy as np

from copy import deepcopy


with open("input") as f:
    blocks = [m.split('\n') for m in f.read().split('\n\n')]

ops = {0: lambda x: x * 17,
       1: lambda x: x + 5,
       2: lambda x: x + 8,
       3: lambda x: x + 1,
       4: lambda x: x + 4,
       5: lambda x: x * 7,
       6: lambda x: x + 6,
       7: lambda x: x * x}

_monkeys = {m: {"items": list(map(int, re.findall(r'\d+', lines[1]))),
                "test4": int(lines[3][21:]),
                True: list(map(int, re.findall(r'\d+', lines[4])))[0],
                False: list(map(int, re.findall(r'\d+', lines[5])))[0],
                "op": ops[m],
                } for m, lines in enumerate(blocks)}

mod = np.prod([m["test4"] for m in _monkeys.values()])


def run(n_rounds):
    monkeys = deepcopy(_monkeys)
    inspected = [0 for _ in range(len(monkeys))]
    for _ in range(n_rounds):
        for i, m in monkeys.items():
            while m["items"]:
                item = m["items"].pop(0)
                inspected[i] += 1
                item = m["op"](item)
                monkeys[m[item % m["test4"] == 0]]["items"].append(item % mod)
    a, b = sorted(inspected)[-2:]
    return a * b


# part I
print(run(20))

# part II
print(run(10_000))