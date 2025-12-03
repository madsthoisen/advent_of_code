with open("input") as f:
    rotations = [(line[0], int(line[1:])) for line in f.readlines()]


dirs = {'L': -1, 'R': 1}
p = 50
p1, p2 = 0, 0
for d, val in rotations:
    for _ in range(val):
        p = (p + dirs[d] * 1) % 100
        p2 += p == 0
    p1 += p == 0

# part I
print(p1)

# part II
print(p2)
