import re
from collections import defaultdict
from itertools import count


with open("input") as f:
    steps = sorted([re.findall('[A-Z]', line)[1:] for line in f.readlines()])


requirements = defaultdict(set)
incomplete = set()
for k, v in steps:
    requirements[v].add(k)
    incomplete = incomplete.union({k, v})
l = len(incomplete)

# part I
complete = []
incomplete_tmp = incomplete.copy()
while incomplete_tmp:
    for x in sorted(incomplete_tmp):
        req = requirements[x]
        if req.issubset(complete):
            incomplete_tmp.remove(x)
            complete.append(x)
print(''.join(complete))


# part II
n_workers = 5
additional_time = 60
workers = {i: (0, '') for i in range(n_workers)}
complete = set()
for t in count():
    for worker, (r, step) in workers.items():
        if r == 0:
            if step != '':
                complete.add(step)
            workers[worker] = (0, '')
            for x in sorted(incomplete):
                if requirements[x].issubset(complete):
                    workers[worker] = (additional_time + ord(x) - 64 - 1, x)
                    incomplete.remove(x)
                    break
        else:
            if step:
                workers[worker] = (r - 1, step)
    if len(complete) == l:
        print(t)
        break
