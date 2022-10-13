import numpy as np

from collections import OrderedDict

# part I
n_elves = 3_005_290
elves = np.array(list(range(n_elves)))
while True:
    if len(elves) in {1, 3}:
        print(elves[-1] + 1)
        break
    if len(elves) % 2:
        elves = elves[2::2]
    else:
        elves = elves[::2]


# part II

# pattern spotting:
for n_elves in range(1, 100):
    elves = list(range(1, n_elves + 1))
    l = len(elves)
    i = 0
    while l > 1:
        pop_index = (i + l // 2) % l
        if pop_index > i:
            i += 1
        elves.pop(pop_index)
        l -= 1
        i %= l
    print(n_elves, elves[0])


# solving
n = 2
num = 1
for i in range(4, n_elves):
    if num < 3**n:
        num += 1
    if num > 3**(n - 1):
        num += 1
    if num > 3**n:
        num = 1
        n += 1
print(num)

