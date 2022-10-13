with open("input") as f:
    tmp = [g.strip().split("\n") for g in f.read().split("\n\n")]

print(sum(map(len, [set("".join(l)) for l in tmp])))
print(sum(len(set.intersection(*list(map(set, L)))) for L in tmp))
