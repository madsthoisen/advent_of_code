import re

from collections import defaultdict


with open("input") as f:
    n_players, n_marbles = list(map(int, re.findall("\d+", f.read())))


def insert_marble(ll, marble_n, marble_c):
    before = ll[marble_c][1]
    after = ll[before][1]
    ll[before][1] = marble_n
    ll[after][0] = marble_n
    ll[marble_n] = [before, after]
    return ll, marble_n


def special(ll, marble_n, marble_c):
    for _ in range(7):
        marble_c = ll[marble_c][0]
    before, after = ll[marble_c][0], ll[marble_c][1]
    ll[before][1] = after
    ll[after][0] = before
    return ll, after, marble_n + marble_c


def winner(n_players, n_marbles):
    player, marble_c = 2, 1
    ll = {0: [1, 1], 1: [0, 0]}
    points = defaultdict(int)
    for marble_n in range(2, n_marbles + 1):
        if not marble_n % 23:
            ll, marble_c, p = special(ll, marble_n, marble_c)
            points[player] += p
        else:
            ll, marble_c = insert_marble(ll, marble_n, marble_c)
        player = (player + 1) % n_players
    return max(points.values())


# part I
print(winner(n_players, n_marbles))

# part II
print(winner(n_players, 100*n_marbles))
