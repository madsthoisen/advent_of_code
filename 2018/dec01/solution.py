with open("input") as f:
    L = [int(x) for x in f.readlines()]


# part I
print(sum(L))

# part II
f = 0
i = 0
seen = set()
while f not in seen:
    seen.add(f)
    f += L[i % len(L)]
    i += 1
print(f)

