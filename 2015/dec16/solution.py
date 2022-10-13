import re

with open("input") as f:
    tmp = [l.strip() for l in f.readlines()]
    aunts = [re.split(r": ([a-z])", l) for l in tmp]
    aunts = {k[4:]: (v1 + v2).split(", ") for k, v1, v2 in aunts}

for aunt, att in aunts.items():
    aunts[aunt] = {el.split(": ")[0]: el.split(": ")[1] for el in att}

with open("ticker_tape") as f:
    tmp = [line.strip() for line in f.readlines()]
    ticker_tape = {l.split(": ")[0]: l.split(": ")[1] for l in tmp}

# part I
new_aunts = aunts.copy()
for aunt, att in aunts.items():
    if any(val != ticker_tape[a] for a, val in att.items()):
        del new_aunts[aunt]

print(list(new_aunts.keys())[0])

# part II
new_aunts = aunts.copy()
for aunt, att in aunts.items():
    for a, val in att.items():
        if a in {"cats", "trees"}:
            if val <= ticker_tape[a] and aunt in new_aunts:
                del new_aunts[aunt]
        elif a in {"pomerians", "goldfish"}:
            if val >= ticker_tape[a] and aunt in new_aunts:
                del new_aunts[aunt]
        else:
            if val != ticker_tape[a] and aunt in new_aunts:
                del new_aunts[aunt]

print(list(new_aunts.keys())[0])
