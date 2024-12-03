import re


with open("input") as f:
    instructions = f.read()


def execute(part2):
    do = True
    add = 0
    for a, b, ins in re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", instructions):
        if a and b and do:
            add += int(a) * int(b)
        elif part2:
            do = ins == 'do()'
    return add


# part I
print(execute(False))


# part II
print(execute(True))
