with open("input") as f:
    rps = [line.strip().split() for line in f.readlines()]


trans = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
points = {'R': 1, 'P': 2, 'S': 3}
wins = {'R': 'S', 'S': 'P', 'P': 'R'}
loses = {v: k for k, v in wins.items()}


def score(a, b, part):
    opp = trans[a]
    if part == 1:
        you = trans[b]
    elif part == 2:
        if b == 'X':
            you = wins[opp]
        elif b == 'Y':
            you = opp
        elif b == 'Z':
            you = loses[opp]

    if wins[you] == opp:
        return points[you] + 6
    elif you == opp:
        return points[you] + 3
    return points[you]


# part I
print(sum(score(a, b, 1) for a, b in rps))


# part II
print(sum(score(a, b, 2) for a, b in rps))

