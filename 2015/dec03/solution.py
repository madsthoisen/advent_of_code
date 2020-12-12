with open("input") as f:
    tmp = f.read().strip()

dirs = {'<': -1, '>': 1, '^': 1j, 'v': -1j}

# part I
pos = 0
houses = {pos}
for d in tmp:
    pos += dirs[d]
    houses.add(pos)
print(len(houses))

# part II
pos = [0, 0]
houses = {0}
for i, d in enumerate(tmp):
    pos[i%2] += dirs[d]
    houses.add(pos[i%2])
print(len(houses))


