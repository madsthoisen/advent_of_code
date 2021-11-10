import re

from collections import defaultdict
from hashlib import md5
from itertools import count
from math import inf


def md5_hash(s, depth):
    tmp = md5(s.encode('utf-8')).hexdigest().lower()
    for _ in range(depth - 1):
        tmp = md5(tmp.encode('utf-8')).hexdigest().lower()
    return tmp


def is_key(s, reps, depth):
    assert reps in {3, 5}
    reg = r"(.)\1{2}" if reps == 3 else r"(.)\1{4}"
    return re.findall(reg, md5_hash(s, depth))


def run(depth):
    threes = defaultdict(list)
    keys = set()
    i = 0
    stop = inf
    while i - stop <= 1000:
        i += 1
        for five in is_key(input_str + str(i), 5, depth):
            for last in threes[five]:
                if i - last <= 1000:
                    keys.add(last)
                    if len(keys) == 64:
                        stop = i
        if (three := is_key(input_str + str(i), 3, depth)):
            threes[three[0]].append(i)
    return sorted(list(keys))[63]


input_str = "cuanljph"

# part I
print(run(1))

# part II
print(run(2017))
