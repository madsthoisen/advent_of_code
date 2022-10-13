import sys
sys.setrecursionlimit(10000)

with open("input") as f:
    tmp = f.read().split("\n\n")
    p1, p2 = [list(map(int, p.strip().split('\n')[1:])) for p in tmp]


def round(p1, p2):
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        return p1 + [c1, c2], p2
    return p1, p2 + [c2, c1]

def points(p):
    return sum(p[i] * (len(p) - i) for i in range(len(p)))

def play(p1, p2):
    while True:
        p1, p2 = round(p1, p2)
        if len(p1) == 0:
            return points(p2)
        if len(p2) == 0:
            return points(p1)

def play_rec(p1, p2, history):
    state = (tuple(p1), tuple(p2))
    if state in history:
        return 1, points(p1), history
    history.add(state)

    if len(p1) == 0:
         return 2, points(p2), history
    if len(p2) == 0:
         return 1, points(p1), history

    c1, c2 = p1.pop(0), p2.pop(0)

    if (len(p1) >= c1 and len(p2) >= c2):
        winner, _, _ = play_rec(p1[:c1], p2[:c2], set())
        if winner == 1:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    else:
        if c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    return play_rec(p1, p2, history)


# part I
print(play(p1.copy(), p2.copy()))

# part II
winner, score, history = play_rec(p1.copy(), p2.copy(), set())
print(score)
