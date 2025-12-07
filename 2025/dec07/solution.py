from collections import defaultdict


with open("input") as f:
    ll = [line.strip() for line in f.readlines()]


n_splits = 0
s_idx = next(i for i, val in enumerate(ll[0]) if val == 'S')
beams = {s_idx: 1}
while ll:
    splitters = {i for i, val in enumerate(ll.pop(0)) if val == '^'}
    new_beams = defaultdict(int)
    for i, amnt in beams.items():
        if i in splitters:
            n_splits += 1
            new_beams[i - 1] += amnt
            new_beams[i + 1] += amnt
        else:
            new_beams[i] += amnt
    beams = new_beams

# part I
print(n_splits)

# part II
print(sum(beams.values()))
