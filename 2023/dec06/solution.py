import numpy as np
import re
from math import sqrt

with open("input") as f:
    time, dist = [re.findall("\d+", line) for line in f.readlines()]


def n_beats(t, d):
    sd = sqrt(t**2 - 4*d)
    return int((t + sd) // 2 - (t - sd) // 2)


# part I
tt, dd = map(int, time), map(int, dist)
print(np.prod(list(n_beats(t, d) for t, d in zip(tt, dd))))

# part II
t, d = int(''.join(time)), int(''.join(dist))
print(n_beats(t, d))
