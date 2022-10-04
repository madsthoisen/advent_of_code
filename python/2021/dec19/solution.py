import numpy as np

from itertools import permutations, product


with open("input") as f:
    data = [s.split("\n")[1:] for s in f.read().strip().split("\n\n")]


scanners = {i: np.array([np.array(list(map(int, x.split(',')))) for x in scanner]) for i, scanner in enumerate(data)}


changes = []
for m in product([-1, 1], repeat=3):
    for perm in permutations([0, 1, 2], 3):
        if np.linalg.det(M := np.diag(m)[:, perm]) > 0:
            changes.append(M)

def get_var(s):
    for M in changes:
        yield np.matmul(s, M)


all_points = set([tuple(x) for x in scanners[0]])
del scanners[0]
positions = [np.array([0, 0, 0])]
while scanners:
    new_scanners = dict(scanners)
    for i, s in scanners.items():
        found = False
        for var in get_var(s):
            for q in all_points:
                for p in var:
                    translate = q - p
                    new_points = set([tuple(x + translate) for x in var])
                    overlap = all_points.intersection(new_points)
                    if len(overlap) >= 12:
                        all_points = all_points.union(new_points)
                        positions.append(translate)
                        found = True
                        del new_scanners[i]
                        break
                if found:
                    break
            if found:
                break
    scanners = dict(new_scanners)

# part I
print(len(all_points))

# part II 
def manh(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

print(max(manh(s1, s2) for s1 in positions for s2 in positions))
