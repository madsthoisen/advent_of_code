import re

with open("input") as f:
    triangles = [list(map(int, re.findall(r"\d+", line.strip())))
                 for line in f.readlines()]

# part I
sorted_triangles = [sorted(t) for t in triangles]
valid = [t for t in sorted_triangles if t[0] + t[1] > t[2]]
print(len(valid))

# part II
l = len(triangles)
new_triangles = []
cols = [[triangles[r][c] for r in range(l)] for c in range(3)]
for col in cols:
   tmp = [sorted(col[i : i + 3]) for i in range(0, l - 2, 3)]
   new_triangles.extend(tmp)
valid = [t for t in new_triangles if t[0] + t[1] > t[2]]
print(len(valid))
