with open("input") as f:
    moves = f.read()


def shape(r, y):
    shapes = {1: {(2, y), (3, y), (4, y), (5, y)},  # horizontal bar
              2: {(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)},  # plus
              3: {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)},  # angle
              4: {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)},  # vertical bar
              0: {(2, y), (3, y), (2, y + 1), (3, y + 1)}}  # box
    return shapes[r]


# part I
N = 2022
max_y = 0
tetris = set()
m = 0
for r in range(1, N + 1):
    s = shape(r % 5, max_y + 4)
    while True:
        move = moves[m % len(moves)]
        if move == '<':
            new_s = {(x - 1, y) for x, y in s}
            if all([x >= 0 for x, _ in new_s]) and not new_s & tetris:
                s = new_s
        elif move == '>':
            new_s = {(x + 1, y) for x, y in s}
            if all([x < 7 for x, _ in new_s]) and not new_s & tetris:
                s = new_s
        m += 1
        new_s = {(x, y - 1) for x, y in s}
        if any([y <= 0 for _, y in new_s]) or new_s & tetris:
            break
        s = new_s
    tetris |= s
    max_y = max(y for _, y in tetris)

print(max_y)


# part II

# printing the height when m % len(moves) == 0 prints:
# 1739 2736
# 3484 5486
# 5229 8236
# ...
# revealing that every 1745th piece, max_y increases with 2750.
# Thus, the answer to part II is the sum of:
# - the height at 1739: 2736
# - 2750 times n_rounds (n_rounds = (1000000000000 - 1739) // 1745)
# - the height increase from 1739 + 2750*n_rounds to 1000000000000
#   which is the same as the height increase from round 1739 to 1000000000000 - n_rounds * 1745
#   which is 4326 - 2736 = 1590

num = 1000000000000
n_rounds = (num - 1739) // 1745
print(2736 + 2750 * n_rounds + 1590)
