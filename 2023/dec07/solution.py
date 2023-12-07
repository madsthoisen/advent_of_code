from itertools import combinations_with_replacement

from collections import Counter


with open("input") as f:
    lines = [(list(h), int(r)) for h, r in (line.strip().split(' ') for line in f.readlines())]

vals = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
ranks = {(5,): 6, (1, 4): 5, (2, 3): 4, (1, 1, 3): 3, (1, 2, 2): 2, (1, 1, 1, 2): 1, (1, 1, 1, 1, 1): 0}


def kind(hand, part2=False):
    card_vals = [vals[x] for x in hand]
    if part2:
        vals['J'] = -1
        hand = [x for x in hand if x != 'J']
    combs = combinations_with_replacement(set(vals.keys() - {'J'}), 5 - len(hand))
    return max([ranks[tuple(sorted(Counter(hand + list(add)).values()))]] + card_vals for add in combs)


# part I
xx = sorted(lines,  key=lambda x: kind(x[0]))
print(sum((i + 1) * r for i, (_, r) in enumerate(xx)))

# part II
xx = sorted(lines,  key=lambda x: kind(x[0], True))
print(sum((i + 1) * r for i, (_, r) in enumerate(xx)))

