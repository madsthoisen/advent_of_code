from itertools import combinations_with_replacement

from collections import Counter


with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

vals = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
ranks = {(5,): 6, (1, 4): 5, (2, 3): 4, (1, 1, 3): 3, (1, 2, 2): 2, (1, 1, 1, 2): 1, (1, 1, 1, 1, 1): 0}


def kind(hand, part2=False):
    card_vals = tuple(vals[x] for x in hand)
    if part2:
        vals['J'] = -1
        hand = [x for x in hand if x != 'J']
    cards_no_joker = set(vals.keys()) - {'J'}
    ranks_possible = []
    for add in list(combinations_with_replacement(cards_no_joker, 5 - len(hand))) + []:
        rank = tuple(sorted(Counter(hand + list(add)).values()))
        ranks_possible.append((ranks[rank],) + card_vals)
    return max(ranks_possible)


# part I
xx = {kind(list(hand), False): int(b) for hand, b in lines}
print(sum((i + 1) * xx[rank] for i, rank in enumerate(sorted(xx.keys()))))


xx = {kind(list(hand), True): int(b) for hand, b in lines}
print(sum((i + 1) * xx[rank] for i, rank in enumerate(sorted(xx.keys()))))
