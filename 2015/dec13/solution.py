from collections import defaultdict
from itertools import permutations


with open("input") as f:
    increases = [line.strip().split(' ') for line in f.readlines()]


G = defaultdict(int)
for line in increases:
    a, b, mode, val = line[0], line[-1][:-1], line[2], line[3]
    G[(a, b)] += int(val)*(1 if mode == "gain" else -1)


def increase(seating):
    return sum(G[(a, b)] + G[(b, a)] for a, b in zip(seating, seating[1:] + (seating[0],)))


# part I
people = {a for a, _ in G}
print(max(increase(seating) for seating in permutations(people)))

# part II
for p in people:
    G[("me", p)] = 0
people.add("me")
print(max(increase(seating) for seating in permutations(people)))
