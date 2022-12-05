import re

from collections import defaultdict


with open("input") as f:
    stacks, ins = f.read().split("\n\n")
    ins = [map(int, re.findall("\d+", line)) for line in ins.split('\n')]

ll = defaultdict(list)
for s in stacks.split('\n'):
    for i in range(9):
        crate = s[1 + 4*i]
        if crate != ' ':
            ll[i + 1].append(crate)

s1, s2 = dict(ll), dict(ll)
for n, a, b in ins:
    for _ in range(n):
        s1[b] = [s1[a][0]] + s1[b]
        s1[a] = s1[a][1:]
    s2[b] = s2[a][:n] + s2[b]
    s2[a] = s2[a][n:]

# part I
print(''.join(str(s1[i][0]) for i in range(1, 10)))

# part II
print(''.join(str(s2[i][0]) for i in range(1, 10)))