import re

from z3 import Bool, If, Int, Optimize, Sum


with open("input") as f:
    lines = [list(map(int, re.findall("-?\d+", line))) for line in f.readlines()]


def manh(x, y):
    return sum(abs(xi - yi) for xi, yi in zip(x, y))


bots = {(x, y, z): r for x, y, z, r in lines}

# part I
bot_largest_r = max(bots, key=bots.get)
print(sum(manh(b, bot_largest_r) <= bots[bot_largest_r] for b in bots))


# part II
def z3manh(x, y):
    z3abs = lambda x: If(x < 0, -x, x)
    return sum(z3abs(xi - yi) for xi, yi in zip(x, y))


model = Optimize()
x, y, z = Int('x'), Int('y'), Int('z')
in_ranges = [Int(f"in_range_{i}") for i in range(len(lines))]

for i, (x1, y1, z1, r) in enumerate(lines):
    model.add(in_ranges[i] == If(z3manh((x, y, z), (x1, y1, z1)) <= r, 1, 0))
count_in_range = Sum(in_ranges)

model.maximize(count_in_range)
model.minimize(z3manh((x, y, z), (0, 0, 0)))
model.check()

print(abs(model.model()[x].as_long()) + abs(model.model()[y].as_long()) + abs(model.model()[z].as_long()))