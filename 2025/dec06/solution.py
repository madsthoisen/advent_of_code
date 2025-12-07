from operator import add, mul
from functools import reduce


with open("input") as f:
    ll = [line.strip('\n') for line in f.readlines()]


p1, p2 = 0, 0
ops = ll.pop(-1)
ops_loc = [i for i, val in enumerate(ops) if val != ' ']
for i, idx in enumerate(ops_loc):
    j = ops_loc[i + 1] if i + 1 < len(ops_loc) else len(ops) + 1
    nums = [line[idx:j - 1] for line in ll]
    op = mul if ops[idx] == '*' else add
    p1 += reduce(op, map(int, nums))
    n = [int(''.join(num[pos] for num in nums)) for pos in range(-1, idx - j, -1)]
    p2 += reduce(op, n)

# part I
print(p1)

# part II
print(p2)