import re

from itertools import count


with open("input") as f:
    replacements, molecule = f.read().strip().split("\n\n")
    replacements = [x.split(' => ') for x in replacements.split("\n")]


def step(molecule):
    return {molecule[:m.start()] + v + molecule[m.end():] for k, v in replacements for m in re.finditer(k, molecule)}


# part I
print(len(step(molecule)))

# part II - Greedy approach with longest substitution in reverse direction works
replacements = [x[::-1] for x in replacements]
molecules = {molecule}
for i in count(1):
    molecules = step(min(molecules, key=len))
    if 'e' in molecules:
        print(i)
        break
