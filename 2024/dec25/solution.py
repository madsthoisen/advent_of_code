with open("input") as f:
    blocks = [b.split("\n") for b in f.read().split("\n\n")]


keys, locks = [], []
for b in blocks:
    ll = [x.count("#") for x in zip(*b)]
    if b[0] == '#####':
        keys.append(ll)
    if b[-1] == '#####':
        locks.append(ll)

# part I
print(sum(all(a + b <= 7 for a, b in zip(k, l)) for k in keys for l in locks))
