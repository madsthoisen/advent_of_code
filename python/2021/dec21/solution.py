from collections import defaultdict
from itertools import product


with open("input") as f:
    p1_, p2_ = [int(line.strip()[-1]) for line in f.readlines()]


def get_pos(p, v):
    p = (p + v) % 10
    return p if p != 0 else 10


def roll(d, r):
    roll_sum = 0
    for _ in range(3):
        roll_sum += d
        d = d + 1 if d != 100 else 1
    return roll_sum, d, r + 3


# part I
p1, p2 = p1_, p2_
s1, s2 = 0, 0
d, r = 1, 0
win = 1000
while True:
    roll_sum, d, r = roll(d, r)
    p1 = get_pos(p1, roll_sum)
    s1 += p1
    if s1 >= win:
        print(r * s2)
        break
    roll_sum, d, r = roll(d, r)
    p2 = get_pos(p2, roll_sum)
    s2 += p2
    if s2 >= win:
        print(r * s1)
        break
        

# part II
p1, p2 = p1_, p2_
pos = defaultdict(int)
for a in product([1, 2, 3], repeat=3):
    pos[sum(a)] += 1

win = 21
scores = {(p1, 0, p2, 0): 1}
count_p1 = 0
count_p2 = 0
while scores:
    new_scores = defaultdict(int)
    for (p1, s1, p2, s2), a in scores.items():
        assert s1 < win and s2 < win
        for v1, a1 in pos.items():
            p1_new = get_pos(p1, v1)
            s1_new = s1 + p1_new
            if s1_new >= win:
                count_p1 += a * a1
                continue
            for v2, a2 in pos.items():
                p2_new = get_pos(p2, v2)
                s2_new = s2 + p2_new
                if s2_new >= win:
                    count_p2 += a * a1 * a2
                else:
                    new_scores[(p1_new, s1_new, p2_new, s2_new)] += a*a1*a2

    scores = new_scores 
print(count_p1, count_p2)

