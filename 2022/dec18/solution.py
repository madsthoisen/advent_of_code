import numpy as np
import re


with open("input") as f:
    coll = set(tuple(map(int, re.findall("-?\d+", line))) for line in f.readlines())


inc = [np.array([i*x, i*y, i*z]) for x, y, z in [(1, 0, 0), (0, 1, 0), (0, 0, 1)] for i in [-1, 1]]

# part I
print(sum(tuple(z + np.array(l)) not in coll for l in coll for z in inc))

# part II
mins = [min(x[i] for x in coll) for i in range(3)]
maxes = [max(x[i] for x in coll) for i in range(3)]

# find the inside cubes
insides = set()
for x in range(mins[0], maxes[0] + 1):
    for y in range(mins[1], maxes[1] + 1):
        for z in range(mins[2], maxes[2] + 1):
            if (x, y, z) not in coll:
                arr = np.array([x, y, z])
                inside = True
                for w in inc:
                    i = 1
                    while True:
                        p = tuple(arr + i * w)
                        if p in coll:
                            break
                        if any([p[i] < mins[i] for i in range(3)]) or any([p[i] > maxes[i] for i in range(3)]):
                            inside = False
                            break
                        i += 1
                if inside:
                    insides.add((x, y, z))

# find the inside cubes that touches the outside
outsides = set(l for l in insides for z in inc if tuple(z + np.array(l)) not in coll.union(insides))
insides -= outsides

# continuously find the inside cubes that touches the outside
while True:
    outsides = set(l for l in insides for z in inc if tuple(z + np.array(l)) in outsides)
    insides -= outsides
    if not outsides:
        break

print(sum(tuple(z + np.array(l)) not in coll.union(insides) for l in coll for z in inc))