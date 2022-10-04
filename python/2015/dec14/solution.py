import re

with open("input") as f:
    tmp = [l.strip().split(" can fly ") for l in f.readlines()]
    specs = {el[0]: list(map(int, re.findall(r"\d+", el[1]))) for el in tmp}

reindeers = {k: [0, s[1], 0, 0] for k, s in specs.items()}

T = 2503
for t in range(T):
    for r, status in reindeers.items():
       if status[2] > 0:
           status[2] -= 1
       else:
            status[1] -= 1
            status[0] += specs[r][0]
       if status[1] == 0:
           status[1:3] = specs[r][1:3]
    for r in reindeers:
        if reindeers[r][0] == max(r[0] for r in reindeers.values()):
            reindeers[r][3] += 1

# part I
print(max(r[0] for r in reindeers.values()))

# part II
print(max(r[3] for r in reindeers.values()))
