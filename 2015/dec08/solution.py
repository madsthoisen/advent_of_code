import re


with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]

patterns = [r"\\x[0-9a-fA-F]{2}", r"\\\\", r"\\\""]


def ev(line, part2=False):
    l = len(line)
    d = {0: 5, 1: 4, 2: 4}
    for i, p in enumerate(patterns):
        sub = ' ' * d[i] if part2 else ' '
        line = re.sub(p, sub, line)
    return len(line) - l + 4 if part2 else l - len(line) + 2


# part I
print(sum(ev(x) for x in tmp))

# part II
print(sum(ev(x, True) for x in tmp))
