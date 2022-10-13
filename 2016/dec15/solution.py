import re

from sympy.ntheory.modular import crt


with open("input") as f:
    discs = [list(map(int, re.findall(r'\d+', line))) for line in f.readlines()]


# For all discs we must have that
# (start_position + t + disc_no) % number_of_positions == 0
# This calls for CRT

def solve():
    t, _ = crt([x[1] for x in discs], [-x[0] - x[3] for x in discs])
    return t


# part I
print(solve())


# part II
discs.append([discs[-1][0] + 1, 11, 0, 0])
print(solve())
