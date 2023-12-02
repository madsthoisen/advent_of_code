import numpy as np
from collections import defaultdict

with open("input") as f:
    games = f.read().split("\n")

power_sum = 0
possible = 0
for game in games:
    game_id, cubes = game.split(': ')
    d = defaultdict(int)
    for s in cubes.split('; '):
        for cubes in s.split(', '):
            n, col = cubes.split(' ')
            d[col] = max(d[col], int(n))
    if d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14:
        possible += int(game_id[5:])
    power_sum += np.prod(list(d.values()))

# part I
print(possible)

# part II
print(power_sum)
