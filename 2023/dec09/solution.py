import re


re_numbers_plus_minus = r"-?\d+"


with open("input") as f:
    numbers_from_lines = [list(map(int, re.findall(re_numbers_plus_minus, line))) for line in f.readlines() if line != "\n"]


def get(line):
    lines = [line]
    while any(x != 0 for x in lines[-1]):
        lines.append([b - a for a, b in zip(lines[-1], lines[-1][1:])])
    return lines


ll = [get(line) for line in numbers_from_lines]


# part I
def new(lines):
    new_lines = [lines[-1] + [0]]
    for l in lines[-2::-1]:
        val = new_lines[-1][-1] + l[-1]
        new_lines.append(l + [val])
    return new_lines


print(sum(new(lines)[-1][-1] for lines in ll))


# part II
def new(lines):
    new_lines = [[0] + lines[-1]]
    for l in lines[-1::-1]:
        val = l[0] - new_lines[-1][0]
        new_lines.append([val] + l)
    return new_lines


print(sum(new(lines)[-1][0] for lines in ll))