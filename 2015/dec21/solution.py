from itertools import combinations


with open("input") as f:
    boss = tuple(map(int, [line.strip().split(' ')[-1] for line in f.readlines()]))

weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]


def play(player, boss):
    hp = 100
    while True:
        boss[0] -= max(player[0] - boss[2], 0)
        if boss[0] <= 0:
            return True
        hp -= max(boss[1] - player[1], 0)
        if hp <= 0:
            return False


part_1 = float("inf")
part_2 = 0
for w in weapons:
    for a in armors + [[0, 0, 0]]:
        for r1, r2 in combinations(rings + [[0, 0, 0], [0, 0, 0]], 2):
            gold = w[0] + a[0] + r1[0] + r2[0]
            dam = w[1] + a[1] + r1[1] + r2[1]
            arm = w[2] + a[2] + r1[2] + r2[2]
            if play((dam, arm), list(boss)):
                part_1 = min(part_1, gold)
            else:
                part_2 = max(part_2, gold)

# part I
print(part_1)

# part II
print(part_2)
