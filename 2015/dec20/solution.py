from itertools import count
from sympy import divisors


puzzle_input = 33100000


# part I
print(next(i for i in count(0) if sum(divisors(i)) * 10 >= puzzle_input))


# part II
m = puzzle_input // 11
presents = [0] * m
for elf in range(1, m):
    for a in range(1, 51):
        if (house := elf * a) >= m:
            break
        presents[house] += elf * 11
print(next(i for i, p in enumerate(presents) if p >= puzzle_input))
